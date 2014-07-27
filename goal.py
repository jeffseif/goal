#! /usr/bin/env python3

class G:

    text = 'g'
    
    def __call__(self, end = None):

        self.text += 'o'

        if end is None:
            return self

        return self.text + end

g = lambda arg = None: G() if not(arg) else 'gal'

if __name__ == '__main__':
    print(g()('al'))
