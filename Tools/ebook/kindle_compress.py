"""Make a Kindle copy of an EPUB: the same book, with its images made small enough that Amazon's per-megabyte delivery
fee stays low (a 25 MB EPUB costs about $3.75 a sale on the 70% royalty; its Kindle copy, about 9 MB, about $1.35).

The text is untouched. The chapter-end maps (black line art) become four-grey PNGs at 1,200 px wide, the chapter
openers four-grey PNGs at 1,000 px, and any other image (except the cover) a JPEG at quality 80.

Use:  python3 Tools/ebook/kindle_compress.py "Book 1"            every edition of a book, into "Book 1/Kindle/"
      python3 Tools/ebook/kindle_compress.py IN.epub OUT.epub     one file
"""
import io, sys, zipfile, re
from PIL import Image

def clean(img, w):
    img = img.convert('L')
    if img.width > w:
        img = img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)
    img = img.point(lambda v: 255 if v >= 225 else v)
    return img.point(lambda v: int(round(round(v / 85) * 85)))

def png4(img, w):
    b = io.BytesIO(); clean(img, w).convert('P', palette=Image.ADAPTIVE, colors=4).save(b, 'PNG', optimize=True); return b.getvalue()

def shrink(src, dst):
  zi = zipfile.ZipFile(src)
  renamed = {n.split('/')[-1]: n.split('/')[-1][:-4] + '.png' for n in zi.namelist() if n.split('/')[-1].startswith('map_') and n.endswith('.jpg')}
  with zipfile.ZipFile(dst, 'w') as zo:
      zo.writestr(zi.getinfo('mimetype'), zi.read('mimetype'), compress_type=zipfile.ZIP_STORED)
      items = [i for i in zi.infolist() if i.filename != 'mimetype']
      for i in items:
          n = i.filename; data = zi.read(n); base = n.split('/')[-1]
          if base.startswith('map_') and n.endswith('.jpg'):
              new = n[:-4] + '.png'
              zo.writestr(new, png4(Image.open(io.BytesIO(data)), 1200), compress_type=zipfile.ZIP_STORED)
          elif base.startswith('opener_') and n.endswith('.png'):
              zo.writestr(n, png4(Image.open(io.BytesIO(data)), 1000), compress_type=zipfile.ZIP_STORED)
          elif n.endswith(('.jpg', '.jpeg')) and base != 'cover.jpg':
              b = io.BytesIO(); Image.open(io.BytesIO(data)).convert('L').save(b, 'JPEG', quality=80, optimize=True, progressive=True)
              zo.writestr(n, b.getvalue() if len(b.getvalue()) < len(data) else data, compress_type=zipfile.ZIP_STORED)
          elif n.endswith(('.xhtml', '.opf', '.ncx', '.html')):
              t = data.decode('utf-8')
              for a, b in renamed.items(): t = t.replace(a, b)
              if n.endswith('.opf'):
                  t = re.sub(r'(href="[^"]*map_[^"]*\.png"[^>]*?)media-type="image/jpeg"', r'\1media-type="image/png"', t)
                  t = re.sub(r'media-type="image/jpeg"([^>]*?href="[^"]*map_[^"]*\.png")', r'media-type="image/png"\1', t)
              zo.writestr(i, t.encode('utf-8'), compress_type=zipfile.ZIP_DEFLATED)
          else:
              zo.writestr(i, data, compress_type=zipfile.ZIP_DEFLATED)


if __name__ == "__main__":
    import glob, os
    if len(sys.argv) == 3 and sys.argv[1].endswith(".epub"):
        shrink(sys.argv[1], sys.argv[2])
    else:
        for book in sys.argv[1:]:
            out = os.path.join(book, "Kindle"); os.makedirs(out, exist_ok=True)
            for f in sorted(glob.glob(os.path.join(book, "*", "*.epub"))):
                if os.sep + "Kindle" + os.sep in f:
                    continue
                dst = os.path.join(out, os.path.basename(f))
                shrink(f, dst)
                print(f"{dst}: {os.path.getsize(f) / 1e6:.1f} MB -> {os.path.getsize(dst) / 1e6:.1f} MB")
