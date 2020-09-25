import __main__
import itertools
import string
import os
import tempfile
from typing import List, Tuple, Dict


class Slayer:
    # Tag used for obfuscation
    TAG : str = 'buffy'


    def __init__(self):
        self._base = len(Slayer.TAG)**2

        self._dictTAG = dict(zip(range(self._base), map(lambda s: s + ' ', map(''.join, itertools.product(*((car.lower(), car.upper()) for car in Slayer.TAG))))))
        newKeys = [str(i) for i in range(10)]
        newKeys += [chr(car) for car in range(97, 97 + self._base -10)]
        self._dictTAG = dict(zip(newKeys, self._dictTAG.values()))

        self._reverseDictTAG = {}
        for key, value in self._dictTAG.items():
            self._reverseDictTAG[value.rstrip()] = key

        self._filename = __main__.__file__

        with open(self._filename, 'r') as fic:
            self._data = fic.readlines()

        self._mode = None
        self._modeDetection()


    def _toBase(self, value : int) -> str:
        result = '' 
        while value > 0: 
            result = string.printable[value % self._base] + result
            value = value // self._base 
        return result


    def _fromBase(self, value : str) -> int:
        return int(value, self._base) 


    def _modeDetection(self) -> None:
        """Detect if the file is in read or write
           mode.
        """
        for line in self._data[1:]:
            if line.lower().startswith(f"'{Slayer.TAG}"):
                self._mode = 'r'
            elif not line[0].isspace():
                self._mode = 'w'


    def _obfuscate(self, car : str) -> str:
        """Use TAG as seed to obfuscate a character

        Args:
            car (str): The character to obfuscate

        Returns:
            str: The character obfuscated
        """
        #print(f'{car} => {ord(car)} ... {self._toBase(ord(car))}')
        result = ''
        for n in self._toBase(ord(car)):
            result += self._dictTAG[n]
        return result


    def _deobfuscate(self, tag : Tuple[str]) -> str:
        return chr(self._fromBase(self._reverseDictTAG[tag[0]]) * self._base + self._fromBase(self._reverseDictTAG[tag[1]]))


    def _write(self) -> None:
        """Obfuscate the filename file and write a new file
        self._filename_TAG.py
        """
        output = os.path.splitext(self._filename)[0] + f'_{Slayer.TAG}.py'

        with open(output, 'w') as fic:
            for n, line in enumerate(self._data):
                if n == 0:
                    fic.write(line)
                else:
                    newline = ''
                    for car in line:
                        if car == '\n':
                            newline += car
                        else:
                            newline += self._obfuscate(car)
                    if newline.isspace():
                        fic.write(newline)
                    else:
                        fic.write(f"'{newline}'")
        

    def _read(self) -> None:

        def pairwise(iterable):
            elt = iter(iterable)
            return zip(elt, elt)

        output = ''
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as fic:
            output = fic.name
            for n, line in enumerate(self._data):
                if n == 0:
                    next
                else:
                    newline = ''
                    line = line[1:-1].split(' ')
                    for tag in pairwise(line):
                        newline += self._deobfuscate(tag)
                    fic.write(newline)

        os.system(f'python3 {output}')

        os.unlink(output)


    def action(self) -> None:
        if self._mode == 'r':
            self._read()
        else:
            self._write()



if __name__ == 'Acme.Buffy':
    s = Slayer()
    s.action()
