# simple-stt
A simple speech to text in python, with google stt, and whisper stt and translate

For example, here Google does not recognize me, but whisper can :-)

````
*** reading ***
*** exporting ***
export OK
*** recognizing with google ***
result2:
{   'alternative': [   {   'confidence': 0.81851226,
                           'transcript': 'Bolsover Sugar by Nesta'},
                       {'transcript': 'Bolsover Sugar by Nestor'},
                       {'transcript': 'Bolsover Sugar by investor'},
                       {'transcript': 'Bolsover Sugar by in Leicester'},
                       {'transcript': 'Bolsover Sugar by nister'}],
    'final': True}
Bolsover Sugar by Nesta
 
*** recognizing with whisper ***
{
  "text": "Bonjour Monsieur Google, il fait beau aujourd'hui n'est-ce pas?"
}
*** translating with whisper ***
{
  "text": "Hello Mr. Google, it's a beautiful day today, isn't it?"
}

Process finished with exit code 0
```