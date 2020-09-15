# Rlyehian

_Translate to the language of the "old ones" with the serpent's tong in the digital world._

_Inspired by H.P. Lovecraft_
***

Using the digital serpent's package, you can translate english to the language of the "old ones"

Spread a̶͙̓̓̓͛̿̓͘ḯ̵̡̲̟̼͎̩͉̬̙̈̀͆͜m̴̨̺̖͇͔̝̤̖͊̏̌̅̔̿͜͜͝ģ̶̺͚̬̣̣̜͉̃̒͜ŗ̷͖͇͖̘͍̹̳̈̑͐͌̇̆͘͜͝ͅ'̴̢͉͎͇͔̬̖̽̈̕͜ļ̷̛̥̹̰͎̤͉̫̱̗͗̈́͗͆̾͒̄̅͠ű̸̖̼͇̏̈́̉̊̌̃̕ḩ̷̧̲̬͔̉ͅ


## Getting Started

Follow the scripture below to begin to transcribe into the words of the "old ones".

### Installations

Install the following Serpent dependencies.

1. Install rlyehian
    ```
    $ pip install rlyehian
    ```

If you want to use the projects version of the translator, do the following:
1. Install the Python dependencies:
    ```
    pip install -r requirements.txt
    ```

### Usage

#### Sample Translation Code
Below is a code sample on how to translate english to R'lyehian:

1. Place the following in a python file
    ```bash
        import rlyehian, argparse, os
         
        def main():
            parser = argparse.ArgumentParser(description='Rlyehian Translator.  Speak the language of the old ones.')
            parser.add_argument('-t', '--text', help='Text to Translate', required=True)
            args = vars(parser.parse_args())
            text = args['text']
            ahahog_compendium()
            text = ainghft(text)
            print(text)
         
        if __name__ == "__main__":``
           main()
    ```
2. Run the following command
    ```bash
    $ python test.py -t "I pray to the mother of skin"
    ```
## Current Development

9/7/18 - Simple translation with no checks for word typing.  Only translating in English at the moment.

## Built With

* Python 3.6

## Author

* **Jimmy Le** - [Jldevops](https://github.com/jldevops)

## License

Licensed under the [MIT License](LICENSE)