
ph=open("LetterTemplate.txt","r")
#allows for opening of letter template file
fh=open("StudentNames.txt","r")
#allows for opening of student names file

Breakingnumber=0
#sets value of Breakingnumber to 0

#l=["u,t,e,q,a,g,r,l"]
x=(ph.read(15))
#x reads letter template files first 15 letters
y=(ph.read())
#y reads the rest of the template file
while True:
  Breakingnumber=Breakingnumber+1
  #each time the loop runs 1 is added to breakingnumber
  if Breakingnumber==6:
    break;
    #if breaking number is = 6 the loop will break
  nameinput=input("What is your full name::")
  #creates conditional loop
  print("Please choose a date (Day,Month. Ex: 07,12)")
  #prints asking for user to choose a date
  a=input()
  #a is the input for the date
  print(x, nameinput,y,a)
  o=(x, nameinput,y,a)
  #prints x + line +y +a
  ch=open(nameinput,"a")
  #creates a file with students name as the file name
    
  ch.write(x)
  #write first part of tempalte into file
  ch.write(' ')
  #puts space
  ch.write(nameinput)
  ch.write(' ')
  #writes students name in file
  ch.write(y)
  #writes rest of the template file words
  ch.write(' ')
  #puts space
  ch.write(a)
  #writes the date at the end
  ch.close()
  #closes the newly created file
ph.close()
fh.close()
#clioses files lettertemplate.txt and studentnames.txt