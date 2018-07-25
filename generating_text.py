
generated = sample_text(
  saved_params,
  temperature,  # How risky the network is when generating text
  num_letters=num_letters,
  init_text=text)

seed = "i'm gonna punch lenny in the back of the"

for temperature in [0.2, 0.5, 1.0, 1.2]:
  print("\nGenerating text with riskiness : {}\n".format(temperature))
  print(sample_text(seed, temperature))


"""
Generating text with riskiness : 0.2

i'm gonna punch lenny in the back of the been a to the on the man to the mother and the father to simpson the father to with the marge in the for the like the fame to the been to the for my bart the don't was in the like the for the father the father a was the father been a say the been to me the do it and the father been to go. i want to the boy i can the from a man to be the for the been a like the father to make my bart of the father

Generating text with riskiness : 0.5

i'm gonna punch lenny in the back of the kin't she change and i'm all better it and the was the fad a drivera it? what i want to did hey, he would you would in your bus who know is the like and this don't are for your this all for your manset the for it a man is on the see the will they want to know i'm are for one start of that and i got the better this is. it whoce and i don't are on the mater stop in the from a for the be your mileat

Generating text with riskiness : 1.0

i'm gonna punch lenny in the back of the to to macks how screath. firl done we wouldn't wil that kill. of this torshmobote since, i know i ord did, can give crika of sintenn prescoam.whover my me after may? there's right. that up. there's ruining isay.oh.solls.nan'h those off point chuncing car your anal medion.hey, are exallies a off while bea dolk of sure, hello, no in her, we'll rundems... i'm eventy taving me to too the letberngonce

Generating text with riskiness : 1.2

i'm gonna punch lenny in the back of the burear prespe-nakes, 'lisa to isn't that godios.and when be the bowniday' would lochs meine, mind crikvin' suhle ovotaci!..... hey, a poielyfd othe flancer, this in are rightplouten of of we doll hurrs, truelturone? rake inswaydan justy!we scrikent.ow.. by back hous, smadge, the lighel irely.yes, homer. wel'e esasmoy ryelalrs all wronencay...... nank. i wenth makedyk. come on help cerzind, now, n
"""

