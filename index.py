from apis import *
from apis import plugsurfing
from apis import placetoplug
from apis import plugshare


def main():
   #plugsurfing.load_from_local('data\\plugsurfing_cologne.json')
   #placetoplug.load_from_local('data\\placetoplug_cologne.json')
   plugshare.load_from_local('data\\plugshare_cologne.json')

if __name__ == '__main__':
    main()