# HacknetDialogueCreator
Program converts files written in .txt to proper .xml for Hacknet IRC dialogue.

The .xml file will be created with the same name as .txt input and in the same path.
It will overwrite any existing file with the same name, so bear that in mind while using it.

[Download .exe executable file](https://github.com/mareszm041/HacknetDialogueCreator/raw/master/DialogueCreator/dist/DialogueCreator.exe)

.txt template:
```
<targetComputer><enter>
<delay><single space><name><single : char><message content><enter>
<delay><single space><name><single : char><message content><enter>
<delay><single space><name><single : char><message content><enter>
<and so on...>
```

.txt example input:
```
somecomp
0.6 D3f4ult: Ugh, @channel everyone else running into the brick wall of this whitelist server?
0.4 Coel: Yeah - I think I've got an idea, though. If you can bring it down for a minute or two I'll take care of it.
0.2 D3f4ult: Huh?.
0 D3f4ult: I mean, sure, I can probably sort something out, but, no idea what you're thinking :\
2 Coel: Trade secret ;). You ready? Countdown me
2 D3f4ult: Sure, hold on...
2 D3f4ult: 5
2 D3f4ult: 4
2 D3f4ult: 3
2 D3f4ult: 2
2 D3f4ult: 1
2 D3f4ult: Done, gogogogo
2 Coel: Almost got it...
2 Coel: Annnnd done! We're good to go. Check it for me D3f4ult ?
2 D3f4ult: Holy shit, how?
2 Coel: ;)
2 Coel: Oh yeah, @#PLAYERNAME# - the whitelist server is down!
2 Coel: You should be able to connect to the Bookings Mainframe now
```

.xml output for given example input:
```
<ConditionalActions>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="0.6"> Ugh, @channel everyone else running into the brick wall of this whitelist server?</AddIRCMessage>
  <AddIRCMessage Author="Coel" TargetComp="somecomp" Delay="0.4"> Yeah - I think I've got an idea, though. If you can bring it down for a minute or two I'll take care of it.</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="0.2"> Huh?.</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="0"> I mean, sure, I can probably sort something out, but, no idea what you're thinking :\</AddIRCMessage>
  <AddIRCMessage Author="Coel" TargetComp="somecomp" Delay="2"> Trade secret ;). You ready? Countdown me</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="2"> Sure, hold on...</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="2"> 5</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="2"> 4</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="2"> 3</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="2"> 2</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="2"> 1</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="2"> Done, gogogogo</AddIRCMessage>
  <AddIRCMessage Author="Coel" TargetComp="somecomp" Delay="2"> Almost got it...</AddIRCMessage>
  <AddIRCMessage Author="Coel" TargetComp="somecomp" Delay="2"> Annnnd done! We're good to go. Check it for me D3f4ult ?</AddIRCMessage>
  <AddIRCMessage Author="D3f4ult" TargetComp="somecomp" Delay="2"> Holy shit, how?</AddIRCMessage>
  <AddIRCMessage Author="Coel" TargetComp="somecomp" Delay="2"> ;)</AddIRCMessage>
  <AddIRCMessage Author="Coel" TargetComp="somecomp" Delay="2"> Oh yeah, @#PLAYERNAME# - the whitelist server is down!</AddIRCMessage>
  <AddIRCMessage Author="Coel" TargetComp="somecomp" Delay="2"> You should be able to connect to the Bookings Mainframe now</AddIRCMessage>
</ConditionalActions>
```
