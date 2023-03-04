# simple-stt
A simple speech to text in python, with google stt, and whisper stt and translate

For example, here Google does not recognize me, but whisper can :-)

```
*** reading ***
*** exporting ***
export OK
*** recognizing with google ***
result2:
{   'alternative': [   {   'confidence': 0.21795285,
                           'transcript': 'if it falls on its back'},
                       {'transcript': 'Aether bullseye meaning'},
                       {'transcript': 'Ethan balls army next'},
                       {'transcript': 'Eva balls army next'},
                       {'transcript': 'ether bullseye meaning'}],
    'final': True}
if it falls on its back
 
*** recognizing with whisper ***
Il fait beau aujourd'hui n'est-ce pas?
 
*** translating with whisper ***
It's a beautiful day today, isn't it?

Process finished with exit code 0

```