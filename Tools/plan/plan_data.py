"""Book 1 expanded plan: 79 chapters, six parts, one year. Odd = Maren (S), even = Calder (F).
`old` = the chapter number in the 41-chapter plan this grows from (None = new chapter)."""

PARTS = [
    ("Part One: Two Banks", "Late summer", 1, 12),
    ("Part Two: Harvest of Knives", "Autumn", 13, 26),
    ("Part Three: The Long Autumn", "Autumn into winter", 27, 40),
    ("Part Four: The Frozen River", "Winter", 41, 54),
    ("Part Five: Thaw", "Early spring", 55, 66),
    ("Part Six: The First War", "Spring into summer", 67, 79),
]

C = []
def ch(n, title, beats, echo, old=None):
    C.append(dict(n=n, pov="S" if n % 2 else "F", title=title, beats=beats, echo=echo, old=old))

# ---------------- Part One: Two Banks ----------------
ch(1, "The Unchosen Yard",
   "Training day at Greyhold. Maren wins her bout against Lucan Haverly, but first lance goes to him because he is bonded. Her father's death explains why she never wanted a bond. During the oath, every bonded beast turns its head toward the ground at the words \"the watch below.\" At dusk, fires burn on the far bank.",
   "Seven Clan dragons fly south along the river; the students joke about the trouble across the border.", 1)
ch(2, "Across the River",
   "The same day from the Saltreach bank. The old chief's pyre smoke; the Clan's funeral flight; Ada sings the old song (\"before the six there was one … till the six are one again\"). That night Upper Rush, where Calder's sister Bel lives, is raided for its beasts and burned. Calder finds cart ruts leading to the river and a cut length of beast chain, pockets it, and tells no one.",
   "The knights' lanterns on Greyhold's wall go out one by one. \"They never cross.\"", 2)
ch(3, "The Ferry",
   "Maren crosses at dawn on her mother's ferry to learn what burned. Liss Ashdown, thirty years on the river, gossip at Tolly's Staithe, and the island everyone avoids: Liss's story of why nobody lands on it, and the river-watch law that forbids it. Maren has poled past it a thousand times and never set foot there. Her younger brother Tam sends word he's coming home for the harvest fair.",
   "At the staithe they talk about a Harrow's End farmer who ran two leagues in the dark to his sister's burning farm.")
ch(4, "The Chain",
   "Calder helps Bel and Joss clear the burned barns. Joss swears he'll find his stolen greys. Clan riders come to look, and among them is Teo Varr, the chief's younger son, furious that anyone thinks the Clan did this. Teo notices how Calder calms Joss's terrified mare. Calder nearly shows him the chain, and doesn't.",
   "Across the river, knights ride the bank road in force for the first time in years.")
ch(5, "Roads and Roadblocks",
   "Maren's first patrol on the River Road with Pell. A roadblock of hard men with no colours, checking carts for beasts. Travellers talk of a leader who spoke in a Saltreach port and led a raid in Hearthmere on the same day. The patrol is ordered to let the roadblock be.",
   "A traveller says the Clan's dead chief has a restless brother and two sons who can't stand each other.", 3)
ch(6, "The Uncle and the Sons",
   "Calder carries Harrow's End's grain to Varrhold. He sees both sides: Ulric, the Clan's best warrior with the larger following; Arn's pride; Teo's warmth. He meets the three bonded warriors with their dragons: old Sigrun Holm and Aurveth, hard Dag Rorke and Kharrak, laughing Imra Sallow and Lisska, who teases him about his grain-dust.",
   "A sellsword at the hold complains that the knights have started riding the bank road again.", 4)
ch(7, "The Caged Beast",
   "At Millbrook, where Tam is apprenticed to the smith, Saltreach poachers have caged a young beast and offer Maren a share to look away. She frees it and makes enemies. Tam is dazzled; Pell is not.",
   "The poachers swear to take their grievance \"across the river.\"", 5)
ch(8, "Coldtarn",
   "At the new moon the Clan scatters Haldor's ashes on Coldtarn. Calder carries the village's mourning gift because nobody else will. At the black water Ulric and Arn quarrel in front of everyone and Teo makes them stop. Sigrun tells Calder that Aurveth has outlived two partners and nobody knows how.",
   "In the crowd, a poacher curses a Hearthmere student who freed his catch at Millbrook.")
ch(9, "Pell's Lesson",
   "Pell teaches subdue, don't kill, and shows the class why: the wild wyvern on the Saltreach road that took his fingers, and the knight who killed it and died of it. Tobin, unbonded and bitter, has a pamphlet with two words on it: \"One again.\" Haverly and Kesh, and the shape of a rivalry that isn't hatred.",
   "News across the water: the Clan nearly came to blows at the old chief's ashes.")
ch(10, "Whispers in the Hold",
   "Back at Varrhold with the last of the barley, Calder notices strangers among Ulric's men. One of them, a quiet man called Rook, doesn't belong: wrong boots, wrong hands, and he watches the dragons the way a buyer watches horses.",
   "Poachers in the hold's yard are still cursing the Hearthmere student who freed their catch at Millbrook.", 6)
ch(11, "The Trial",
   "Knight-Captain Ilse Rowan gives Maren her trial: investigate the \"monster\" of the Old Ruin, on its island in the river, and bring back proof. The island is forbidden to the river watch. Liss begs her not to go.",
   "Rowan warns that the Clan's quarrel is coming to a head across the river.", 7)
ch(12, "Harvest",
   "Harrow's End's harvest fair. Wren and Ada; Bel's children, Pip and Nan, dancing. Teo comes with a few riders and stays for the bonfire; he tells Calder he'll meet his uncle at the ford of Hollow Beck to make peace. Calder thinks he might actually manage it.",
   "Hob says a Greyhold boat was seen putting someone onto the Old Ruin's island at dusk, where nobody goes.", None)

# ---------------- Part Two: Harvest of Knives ----------------
ch(13, "The Old Ruin",
   "Maren on the island. The bridge-fort, the broken arches, the verse carved under the tower arch about Winshire. Signs of Restoration hunters: cold fires, cut chains, beast traps.",
   "Smoke rises across the river. Something has happened at the ford.", 9)
ch(14, "The Younger Son",
   "Teo is found dead at the ford of Hollow Beck, apparently killed by Ulric's men on the way to the peace meeting. Arn swears vengeance over his brother's body. Open civil war begins.",
   "The fishermen at Tolly's Staithe say the Greyhold boat is still drawn up on the island.", 8)
ch(15, "Signs",
   "Maren's second day on the island. Tracks bigger than anything she knows. The hunters' camp, empty. Clan war smoke across the water. She sleeps in the tower and counts something enormous breathing in the dark.",
   "War horns from the Saltreach bank all night.")
ch(16, "The Ford",
   "Teo's pyre. The Clan splits: Arn on one side, Ulric on the other. Villages are told to choose. Hob the miller takes Ulric's coin. Calder refuses to choose, which pleases no one.",
   "Hearthmere boats patrol closer to the island than they ever have.")
ch(17, "Night on the Island",
   "The hunters come back, a dozen of them, with chains and a cage on a raft. Maren hides and watches them try to take something in the trees. It goes wrong. Men die. She runs for her boat.",
   "Dragon fire on the far bank: the Clan's first battle has begun.")
ch(18, "Three Deaths",
   "The Clan's battle spills onto the Fenn fields. Sigrun, Dag and Imra die. Their dragons, withering, are drawn to the injured Calder, and three bonds form almost at once. He takes the pull of three deaths.",
   "Through the chaos, a roar rolls across the river from the Old Ruin.", 10)
ch(19, "The Roar",
   "The ancient lion wakes. Maren stands her ground through its roar and doesn't strike. It attacks anyway, and she barely survives.",
   "Three dragons scream across the water, and the sky over the far bank glows.", 11)
ch(20, "Three Voices",
   "Calder wakes with three marks and three grieving, raging minds in his head: Aurveth steady, Kharrak furious, Lisska joking to hide her grief. The village sees what he has become.",
   "The villagers say a monster woke at the Old Ruin the same night.", 12)
ch(21, "Wounded",
   "Restoration hunters chain the wounded lion at the island's tip. Maren breaks a chain and lets it go.",
   "The hunters say they are also after \"the Clan's three loose dragons\" across the river.", 13)
ch(22, "Wren",
   "Wren is the only person in Harrow's End who isn't afraid. Lisska adores her. The village elders want Calder gone. Ada admits the old song has a verse her grandmother taught her and made her swear never to sing.",
   "The fishermen at Tolly's Staithe say someone from Greyhold is still out on the island, and the monster hasn't killed her yet.")
ch(23, "Empty-Handed",
   "Maren could take a lock of the lion's mane as proof but leaves it in peace. The trial is failed; Haverly passes his.",
   "At Greyhold everyone is talking about a farmer bonded to three dragons. No one believes it.", 15)
ch(24, "Hunted",
   "Everyone wants the dragons: Ulric, Arn, Saltreach sellswords, and strangers paying in Restoration coin. Hob sells Calder's whereabouts. He leaves Wren with Ada and flees into the hills.",
   "Lisska spots a knight-student alone at the Old Ruin, with a beast that won't attack her.", 14)
ch(25, "Disgrace",
   "Maren is reassigned to the stables and the midden. Warden Osric Hale of the inner circle takes an interest and asks about the lion.",
   "Hale asks, too carefully, whether she has seen \"the dragon farmer.\"", 17)
ch(26, "Why Me?",
   "In a cave at Crow Scar, Calder asks the dragons why they came to him. None of them knows. Aurveth, who has survived two earlier bonds, has never heard of anything like it.",
   "He hears a Hearthmere student failed her trial rather than harm a monster. It stays with him.", 16)

# ---------------- Part Three: The Long Autumn ----------------
ch(27, "The Stables",
   "Maren learns the bonded beasts by mucking out after them: Kesh's moods, the Darrow girl's hound, the cat nobody owns. Hale teaches her the old history of the orders. She begins to see how bonded and unbonded are not equal anywhere but on the gate.",
   "Refugees from a burned Clan village cross on Liss's ferry.")
ch(28, "Aurveth",
   "Aurveth speaks of her two earlier partners and her oldest memories: the Old Ruin when it was a bridge on the road of the old realm. Kharrak wants Ulric's men dead. Lisska wants to see everything. Calder wants them all quiet.",
   "Lisska reports the knight-student at the island again, sitting with the monster at a distance.")
ch(29, "Without Words",
   "Maren keeps returning to the island. The lion tolerates her at a distance. With no bond, everything between them is action: where she sits, what she doesn't do.",
   "A dragon's shadow passes over the ruin; the lion lifts its head and watches it go.", 21)
ch(30, "The Village Burns",
   "The civil war reaches Harrow's End again, with no winner and only damage. Calder uses the dragons to save people for the first time, and their rage leaks into him.",
   "Knights watch from the far bank and don't cross.", 18)
ch(31, "Tam",
   "Maren visits Tam in Millbrook. He has been to a Restoration meeting in a barn: the unchosen equal, the knights' lies, \"one again.\" They quarrel. Liss's ferry is full of refugees.",
   "The refugees talk of a farmer who brought three dragons down on a burning village, and saved it.")
ch(32, "Sellswords",
   "Captain Idris Vey's company besieges Crow Scar. Kharrak wants to burn them; Calder won't let him. Lisska finds a way out. Calder decides to go south to Wendmouth to find Joss's greys and learn who is buying beasts.",
   "From the heights he sees Hearthmere knights riding out to a burning hamlet on their own bank.")
ch(33, "The Leader",
   "On patrol, Maren glimpses the Restoration's leader at a raid on Ferriby: one man, quiet, precise, directing the raid like a game of stones.",
   "Hearthmere scouts report dragon fire over Harrow's End a week ago.", 19)
ch(34, "The Leader, Again",
   "In Wendmouth, Calder hears the Restoration's leader speak to a crowd: warm, persuasive, a man people want to follow. It is the same day Maren saw him at Ferriby, seventy-five leagues north, though nobody in the crowd can know that.",
   "A beast-seller grumbles about a Hearthmere knight-student up north who sits with monsters instead of killing them.", 20)
ch(35, "The Mentor",
   "Hale tells Maren the history of the oath and lets slip that the inner circle keeps \"a watch nobody else is told about.\" He keeps glancing at the locked cellar door.",
   "Hale has a report from the Saltreach bank: the dragon farmer has left the Marches, heading south.")
ch(36, "Gallows Quay",
   "Wendmouth's beast market. Cages, buyers paying in Restoration coin, and one of Joss's greys. Calder frees the caged beasts, a mirror of Maren at Millbrook, and flees north with the grey and a price on his head.",
   "In the market, sellers curse knights who free other people's property.")
ch(37, "What Hale Won't Say",
   "Hale, grieving a friend or drunk, mentions the legend of the Last Titan and stops short. Maren sees fear in his face.",
   "A report: the dragon farmer is heading north toward the river.", 23)
ch(38, "The Long Road North",
   "Calder and Joss's grey walk north through a country full of Restoration camps. Lisska scouts, Kharrak sulks, Aurveth remembers. A carter mentions the raid on Ferriby, and the date: the day Calder stood in the crowd at Wendmouth. He can't make it add up. He gets home to find Harrow's End half empty and Ada and Wren sheltering at Bel's.",
   "Travellers say a knight-student at Greyhold sits with the Old Ruin's monster and nobody stops her.")
ch(39, "First Frost",
   "In a skirmish the Darrow girl's hound is killed, and over three days the girl withers. Maren sits with her. It is her father's death again, and she can't stop going to the island.",
   "On the night the girl dies, three dragons are seen high over the river, going north.")
ch(40, "The Verse",
   "Lisska remembers the carved verse at the Old Ruin. If anything answers \"why me?\", it's the old realm. Calder decides to go there, as soon as the river lets him.",
   "Lisska says the knight-student and the beast are at the ruin most days now.", 22)

# ---------------- Part Four: The Frozen River ----------------
ch(41, "The Freeze",
   "Deep winter. The Wend freezes from the edges in, and a refugee family tries to walk across. Maren goes out on the ice after them. It breaks. Something huge drags her out of the water and is gone before she can see it.",
   "A dragon lands on the ice upriver and takes off again.")
ch(42, "Crossing the River",
   "Calder crosses the ice to the Old Ruin, hiding the dragons, and narrowly misses Maren and the lion. Each finds only signs of the other.",
   "Footprints, a broken Restoration chain, the lion's scent that makes all three dragons go still.", 24)
ch(43, "Footprints",
   "Maren finds a man's tracks on the island and a dragon scale the size of a shield. She doesn't report either: her first lie to the orders.",
   "The scale is warm.")
ch(44, "The General's Silence",
   "Near the ruin, Aurveth feels something vast and wrong beneath the earth, and won't speak of it.",
   "Through the ice, the dragons hear knights singing at Greyhold: the oath, at midwinter.", 26)
ch(45, "The Accusation",
   "At Millbrook's midwinter fair, the Restoration publicly exposes Hearthmere's secret: a Titan chained beneath the kingdom, its power harnessed for centuries, most of Hearthmere's history built on it. Hearthmere calls it a lie.",
   "The Restoration names \"the dragon farmer\" as proof that the old powers are returning.", 25)
ch(46, "The Forbidden Verse",
   "The accusation reaches Harrow's End. Ada breaks her promise and sings the verse her grandmother made her swear never to sing: the last one sleeps \"where the oath is kept.\" Calder thinks of the knights' oath.",
   "Across the ice, every lamp in Greyhold goes out at once, then comes back.")
ch(47, "Lamps",
   "Hearthmere's magic flickers. The beasts are restless. Riots in Millbrook; knights ordered to arrest Restoration speakers. Tobin disappears from Greyhold.",
   "Rumour: the dragon farmer was seen on the island at the turn of the year.")
ch(48, "Two Sides of a War",
   "Calder tries to make Ulric and Arn stop. Neither will.",
   "Arn mentions a Hearthmere student who keeps company with a monster: \"the kind of madness we could use.\"", 30)
ch(49, "Confession",
   "Maren confronts Hale. He confirms it: the knights' duty \"below\" is guarding the chains.",
   "Hale admits the inner circle fears the dragon farmer almost as much as the Restoration.", 27)
ch(50, "Bel",
   "Joss goes looking for the Restoration camp that holds his other grey and is brought back dead. Bel blames Calder for keeping quiet. He finally shows her the chain and tells her everything: the first thing he has ever chosen to say.",
   "The chain's maker's mark matches the broken chain Calder found on the island in the winter.")
ch(51, "The Door",
   "Hale takes Maren to the locked cellar door. Behind it, far down, the sound of chain. She puts her hand on the door, and across the river the lion roars.",
   "The roar is heard in Harrow's End; the dragons answer it.")
ch(52, "Kharrak",
   "Calder lets Kharrak burn a Restoration beast camp to free its captives. It is the first time he chooses violence. The Restoration names him an enemy.",
   "Across the river, Greyhold's bell rings at night: the knights saw the fire.")
ch(53, "Kin",
   "Maren understands why the lion lingers at the Old Ruin: what lies chained below is its kin. She goes to it knowing her kingdom imprisoned its family.",
   "Fire on the far bank: the farmer's dragons fighting off Restoration hunters.", 29)
ch(54, "The Gathering",
   "Restoration forces mass in the Marches. The civil war is still bleeding the Clan, and Harrow's End is in the path.",
   "Sellswords say they've been paid to bring in \"the knight with the lion\" as well as him.", 28)

# ---------------- Part Five: Thaw ----------------
ch(55, "Thaw",
   "The river breaks up with a noise like cannon. The lion lets Maren close enough to touch. No bond, no words, but it lets her stay.",
   "The Restoration offers a reward for the dragon farmer.")
ch(56, "Wren and the Far-Seer",
   "Lisska perches on the crag above the farm and tells Calder what she sees across the river, and Wren makes him repeat every word. Calder realises his daughter is safer anywhere he isn't.",
   "Lisska reports the knight-student touching the beast's mane.")
ch(57, "Tobin",
   "Maren finds Tobin at a Restoration hedge-meeting. He begs her to join them. She hears the leader speak and he is warm, not precise; she tells herself it's the crowd.",
   "The speaker promises the dragon farmer will \"come home to the one realm.\"")
ch(58, "The Stranger",
   "Calder sees Rook again, the quiet man from Ulric's hall, among Restoration men. He starts to wonder about Teo's death, and has no proof at all.",
   "From the heights he sees Greyhold's walls being raised and armed.")
ch(59, "Orders",
   "Knight-Captain Rowan orders Maren to lure the lion into a trap so the Restoration can't take it. She refuses.",
   "The order also covers \"the farmer with the dragons, if he crosses.\"", 31)
ch(60, "The Ford Again",
   "Calder tries to bring Ulric and Arn to talk at Teo's ford. Someone makes sure it becomes an ambush.",
   "Knights in boats watch the ford and don't cross.")
ch(61, "Lucan",
   "Haverly warns Maren that Rowan will take the lion without her. They talk properly for the first time. He chooses his orders; she understands why.",
   "Haverly says the Clan's ford meeting ended in blood again.")
ch(62, "Before the Storm",
   "Harrow's End prepares to flee. Calder stays near the Old Ruin, where the answers might be, and because the Restoration is hunting him: every league between him and Wren keeps her safer.",
   "Smoke from Greyhold's forges; the knights are arming.", 32)
ch(63, "Broken Oath",
   "Maren breaks the knightly oath to protect the lion and is cast out of Greyhold.",
   "Word arrives that the Restoration's leader is gathering forces at the Old Ruin.", 33)
ch(64, "The Ferry",
   "Ada, Wren and Bel's family cross to Hearthmere as refugees on Liss Ashdown's ferry. Calder watches from the bank. Wren tells the ferrywoman about her father's dragons.",
   "On the Saltreach jetty, while they board, Liss says her daughter was cast out of the knights yesterday for loving a monster.")
ch(65, "Outcast",
   "Maren with Tam in Millbrook, then alone on the island near the lion. Liss tells her about the Saltreach refugees she carried, and a girl called Wren.",
   "Wren's story: her father talks to dragons out loud and they answer.")
ch(66, "The Ruin",
   "Calder leaves the dragons in the Scarfell and goes to the Old Ruin alone to find the answer in the verse. The Restoration arrives in force, and he hides in the tower.",
   "On the island, signs that the knight and the lion left only hours ago.")

# ---------------- Part Six: The First War ----------------
ch(67, "Muster",
   "The Restoration gathers on the island and along the Saltreach bank: boats, ladders, cages. Greyhold arms and shuts its gate. Outcast, Maren watches from the Brackenwood.",
   "The Old Ruin is full of fires and men.")
ch(68, "Two Men",
   "At the Old Ruin, right before the battle, the twins are revealed: the leader in two places was always two men. Hidden, Calder overhears them speak of the killing they arranged in the Dragon Clan. Rook is with them.",
   "They talk of \"the knight's lock\" beneath the school, without saying what it opens.", 34)
ch(69, "War",
   "The Restoration's first open war against the kingdoms breaks out: it crosses the river and drives toward Greyhold and the catacombs. Pell dies holding the gate.",
   "Rumours from the Saltreach side: the dragon farmer has gone to the Old Ruin.", 35)
ch(70, "The Second Lock",
   "Calder learns what the twins are after: two locks, here and beneath the knight school, opened at the same moment. He sends Lisska to warn whoever is at the other lock. She can't speak to anyone but him, so she carries what he can give her: the cut chain from the first night, wrapped in a strip of his shirt with one word burned into it with a coal, TWO, and Wren's blue hair-ribbon. Then he stays to fight.",
   "His choice to warn the student, a stranger he knows only by rumour.", 36)
ch(71, "Millbrook Burns",
   "Millbrook burns. Maren pulls Tam out of the smithy and finds Tobin on the other side of the fight.",
   "Dragon fire over the Old Ruin, two colours of it. She doesn't know yet that a third is missing.")
ch(72, "The Agent",
   "In the fighting at the Ruin, Calder corners Rook. Rook dies before he can say anything useful; the proof dies with him.",
   "The bells of Greyhold stop.")
ch(73, "The Sacrifice",
   "Bond-forcers trap the lion at the edge of the Brackenwood. To save it, Maren offers her own life into the binding in its place. The lion accepts, and the bond forms: for the first time they understand each other. Its name is Orrun.",
   "Lisska lands beside her with a cut chain, a strip of cloth that says TWO, and a child's blue ribbon. Maren knows the ribbon from her mother's story: Wren's. The dragon farmer is warning her.", 37)
ch(74, "Fire at the Ruin",
   "Calder and the dragons fight Corvin Vale at the Old Ruin's lock, and can't stop it opening.",
   "Through the earth, the dragons feel something vast beneath them begin to pull against its chains.", 38)
ch(75, "Through the Cellars",
   "Greyhold is breached. Kesh is killed, and Haverly dies in Maren's arms: one life between two. Hale, dying, gives her the cellar key. She and Orrun go down.",
   "Far below, someone is already at the second lock.")
ch(76, "The Ruin's Lock",
   "Corvin's lock turns. The floor of the Old Ruin falls in, and Calder and the dragons fall with it into the catacombs.",
   "Two locks, one moment.")
ch(77, "The Lock Gives Way",
   "Beneath the school, Maren kills Cassian Vale just as his lock gives way. At the same moment, his brother opens the Old Ruin's lock, and the seal opens. Through the new bond, Maren feels Orrun learn what its kin has become: a world destroyer.",
   "The other lock opening, felt as the seal breaks.", 39)
ch(78, "Underground",
   "The catacombs shake. Coming from opposite ends beneath the border, Calder and Maren meet for the first time.",
   "The stranger he warned, now in front of him.", 40)
ch(79, "The Last Titan",
   "The Last Titan tears free of its chains and flies. Hearthmere's magic begins to fail. The book ends with the two of them watching it go.",
   "Both stories, together for the first time.", 41)

assert [c["n"] for c in C] == list(range(1, 80))
OLD_TO_NEW = {c["old"]: c["n"] for c in C if c["old"]}
