def Zone10(Location_based):
  Select =['corn','chickpeas','mothbeans','lentil','pigeonpeases','mothbeans','blackgram','pomegranate','banana','mango','grapes','watermelon','muskmelon','apples','oranges','papaya','cotton','coconut','jute','coffee']
  fruits = df.loc[:,"label"].unique()
    for fruit in fruits:
  fruit_means[fruit] = df[df['label'] == fruit].mean()
  for fruit in fruits:
    if Select.contains(fruit):
      Location_based[fruit] = df[df['label'] == fruit].mean()
  return Location_based

def Zone9(Location_based):
  Select =['corn','chickpeas','mothbeans','lentil','pigeonpeases','mothbeans','pomegranate','banana','mango','grapes','watermelon','muskmelon','apples','oranges','papaya','cotton']
  fruits = df.loc[:,"label"].unique()
    for fruit in fruits:
  fruit_means[fruit] = df[df['label'] == fruit].mean()
  for fruit in fruits:
    if Select.contains(fruit):
      Location_based[fruit] = df[df['label'] == fruit].mean()
  return Location_based


def Zone8(Location_based):
  Select =['corn','chickpeas','mothbeans','lentil','pomegranate','banana','grapes','watermelon','muskmelon','apples','oranges','cotton']
  fruits = df.loc[:,"label"].unique()
    for fruit in fruits:
  fruit_means[fruit] = df[df['label'] == fruit].mean()
  for fruit in fruits:
    if Select.contains(fruit):
      Location_based[fruit] = df[df['label'] == fruit].mean()
  return Location_based
def Zone7(Location_based):
  Select =['corn','chickpeas','mothbeans','lentil','pomegranate','banana','grapes','watermelon','muskmelon','apples']
  fruits = df.loc[:,"label"].unique()
    for fruit in fruits:
  fruit_means[fruit] = df[df['label'] == fruit].mean()
  for fruit in fruits:
    if Select.contains(fruit):
      Location_based[fruit] = df[df['label'] == fruit].mean()
  return Location_based



def Zone6(Location_based):
  Select =['corn','chickpeas','mothbeans','lentil','banana','grapes','watermelon','muskmelon','apples']
  fruits = df.loc[:,"label"].unique()
    for fruit in fruits:
  fruit_means[fruit] = df[df['label'] == fruit].mean()
  for fruit in fruits:
    if Select.contains(fruit):
      Location_based[fruit] = df[df['label'] == fruit].mean()
  return Location_based

Location_based = {}
def Region(latitude,longitude):
  
if((latitude <= 36.5 and latitude >= 35.5) and (longitude<=103 and longitude >=101)):
  return Zone6(Location_based)
if((latitude <= 35.49 and latitude >= 32) and (longitude<=103 and longitude >=94)):

  return Zone7(Location_based)

if((latitude <= 31.99 and latitude >= 29.5) and (longitude<=106 and longitude >=94)):

  return Zone8(Location_based)

if((latitude <= 29.49 and latitude >= 28) and (longitude<=104 and longitude >=94)):

  return Zone9(Location_based)

if((latitude <= 27.99 and latitude >= 26) and (longitude<=100 and longitude >=97)):

  return Zone10(Location_based)

