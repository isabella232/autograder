test = {
    "name": "test.py",
    "points": 1,
    "suites": [
        {
            "cases": [
                {
                    "code": ">>> main(2)\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 42\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXMXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nUh oh! You blew up!"
                },
                {
                    "code": ">>> main(7)\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 54f\nMines: 9\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXFXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 78f\nMines: 8\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXFXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXFXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 99f\nMines: 7\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXFXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXFXX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 90f\nMines: 6\n  0123456789\n0 XXXXXXXXXF 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXFXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXFXX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 00f\nMines: 5\n  0123456789\n0 FXXXXXXXXF 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXFXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXFXX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 09f\nMines: 4\n  0123456789\n0 FXXXXXXXXF 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXFXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXFXX 8\n9 FXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 77f\nMines: 3\n  0123456789\n0 FXXXXXXXXF 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXFXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXFXX 8\n9 FXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 27\nMines: 3\n  0123456789\n0 FXXXXXXXXF 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXFXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXMXXXXFXX 7\n8 XXXXXXXFXX 8\n9 FXXXXXXXXF 9\n  0123456789\nUh oh! You blew up!"
                },
                {
                    "code": ">>> main(5)\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 54\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXX1XXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 78\nMines: 10\n  0123456789\n0   1XXXXXXX 0\n1  12XXXXXXX 1\n2  2XXXXXXXX 2\n3  2XXXXXXXX 3\n4  1X211XXXX 4\n5  1X1 1111X 5\n6  1X1    2X 6\n7  111    2X 7\n8         11 8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 99\nMines: 10\n  0123456789\n0   1XXXXXXX 0\n1  12XXXXXXX 1\n2  2XXXXXXXX 2\n3  2XXXXXXXX 3\n4  1X211XXXX 4\n5  1X1 1111X 5\n6  1X1    2X 6\n7  111    2X 7\n8         11 8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 67\nMines: 10\n  0123456789\n0   1XXXXXXX 0\n1  12XXXXXXX 1\n2  2XXXXXXXX 2\n3  2XXXXXXXX 3\n4  1X211XXXX 4\n5  1X1 1111X 5\n6  1X1    2X 6\n7  111    2X 7\n8         11 8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 54\nMines: 10\n  0123456789\n0   1XXXXXXX 0\n1  12XXXXXXX 1\n2  2XXXXXXXX 2\n3  2XXXXXXXX 3\n4  1X211XXXX 4\n5  1X1 1111X 5\n6  1X1    2X 6\n7  111    2X 7\n8         11 8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 64\nMines: 10\n  0123456789\n0   1XXXXXXX 0\n1  12XXXXXXX 1\n2  2XXXXXXXX 2\n3  2XXXXXXXX 3\n4  1X211MXXX 4\n5  1X1 1111X 5\n6  1X1    2X 6\n7  111    2X 7\n8         11 8\n9            9\n  0123456789\nUh oh! You blew up!"
                },
                {
                    "code": ">>> main(5)\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 100\nInvalid input. Enter your move (for help enter \"H\"): -100\nInvalid input. Enter your move (for help enter \"H\"): 8f4\nInvalid input. Enter your move (for help enter \"H\"): 4561\nInvalid input. Enter your move (for help enter \"H\"): f43\nInvalid input. Enter your move (for help enter \"H\"): H12\nInvalid input. Enter your move (for help enter \"H\"): H\nFirst, enter the column, followed by the row. To add or remove a flag, add \"f\" after the row (for example, 64f would place a flag on the 6th column, 4th row). Enter your move: 98f\nMines: 9\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXF 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 64\nMines: 9\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXMXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXF 8\n9 XXXXXXXXXX 9\n  0123456789\nUh oh! You blew up!"
                },
                {
                    "code": ">>> main(5)\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 00f\nMines: 9\n  0123456789\n0 FXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 11f\nMines: 8\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 22f\nMines: 7\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 33f\nMines: 6\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 44f\nMines: 5\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 55f\nMines: 4\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 66f\nMines: 3\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 77f\nMines: 2\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 88f\nMines: 1\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 99f\nMines: 0\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 55\nMines: 0\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 33\nMines: 0\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 54f\nYou have already flagged all your mines.\nMines: 0\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 45f\nYou have already flagged all your mines.\nMines: 0\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXFXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 22f\nMines: 1\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXFXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 33f\nMines: 2\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXF 9\n  0123456789\nEnter your move (for help enter \"H\"): 22\nMines: 2\n  0123456789\n0 FXXXXXXXXX 0\n1 XFXXXXXXXX 1\n2 XXMXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXFXXXXX 4\n5 XXXXXFXXXX 5\n6 XXXXXXFXXX 6\n7 XXXXXXXFXX 7\n8 XXXXXXXXFX 8\n9 XXXXXXXXXF 9\n  0123456789\nUh oh! You blew up!"
                },
                {
                    "code": ">>> main(1)\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 55\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXX1XXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 33\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXX1XXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXX1XXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 66\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXX1XXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXX1XXXX 5\n6 XXXXXX2XXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 47\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXX1XXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXX1XXXX 5\n6 XXXXXX2XXX 6\n7 XXXX2XXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 89\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXX2222X 2\n3 XXX1X1  11 3\n4 XXXXX1     4\n5 XXXXX1211  5\n6 XXXXXX2X1  6\n7 112X21211  7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 30\nMines: 10\n  0123456789\n0      1XXXX 0\n1      1XXXX 1\n2    112222X 2\n3    1X1  11 3\n4  112X1     4\n5 12XXX1211  5\n6 XXXXXX2X1  6\n7 112X21211  7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 26\nMines: 10\n  0123456789\n0      1XXXX 0\n1      1XXXX 1\n2    112222X 2\n3    1X1  11 3\n4  112X1     4\n5 12XXX1211  5\n6 XX3XXX2X1  6\n7 112X21211  7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 71\nMines: 10\n  0123456789\n0      1XXXX 0\n1      1XMXX 1\n2    112222X 2\n3    1X1  11 3\n4  112X1     4\n5 12XXX1211  5\n6 XX3XXX2X1  6\n7 112X21211  7\n8   111      8\n9            9\n  0123456789\nUh oh! You blew up!"
                },
                {
                    "code": ">>> main(6)\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXXXXXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 34\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXXXXXX 3\n4 XXX2XXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 63\nMines: 10\n  0123456789\n0 XXXXXXXXXX 0\n1 XXXXXXXXXX 1\n2 XXXXXXXXXX 2\n3 XXXXXX1XXX 3\n4 XXX2XXXXXX 4\n5 XXXXXXXXXX 5\n6 XXXXXXXXXX 6\n7 XXXXXXXXXX 7\n8 XXXXXXXXXX 8\n9 XXXXXXXXXX 9\n  0123456789\nEnter your move (for help enter \"H\"): 78\nMines: 10\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XX1    4\n5  1XXXX21   5\n6  13XXXX1   6\n7   2X2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 37f\nMines: 9\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XX1    4\n5  1XXXX21   5\n6  13XXXX1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 36f\nMines: 8\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XX1    4\n5  1XXXX21   5\n6  13FXXX1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 46\nMines: 8\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XX1    4\n5  1XXXX21   5\n6  13F2XX1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 56\nMines: 8\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XX1    4\n5  1XXXX21   5\n6  13F21X1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 66f\nMines: 7\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XX1    4\n5  1XXXX21   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 54f\nMines: 6\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XF1    4\n5  1XXXX21   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 55\nMines: 6\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XF1    4\n5  1XXX221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 53\nMines: 6\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XF1    4\n5  1XXX221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 54\nMines: 6\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XF1    4\n5  1XXX221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 35\nMines: 6\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XF1    4\n5  1X2X221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 45\nMines: 6\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X2XF1    4\n5  1X22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 44\nMines: 6\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X22F1    4\n5  1X22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 25f\nMines: 5\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 11XXX21    3\n4  1X22F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 23\nMines: 5\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 111XX21    3\n4  1X22F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 24\nMines: 5\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 111XX21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 33\nMines: 5\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 1111X21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 43f\nMines: 4\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XXXXX1     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 22\nMines: 4\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XX1XX1     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 32\nMines: 4\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XX11X1     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 42\nMines: 4\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XX1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 12f\nMines: 3\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 XF1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 02\nMines: 3\n  0123456789\n0 XXXXX1     0\n1 XXXXX1     1\n2 2F1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 11\nMines: 3\n  0123456789\n0 XXXXX1     0\n1 X3XXX1     1\n2 2F1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 21\nMines: 3\n  0123456789\n0 XXXXX1     0\n1 X31XX1     1\n2 2F1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 31\nMines: 3\n  0123456789\n0 XXXXX1     0\n1 X311X1     1\n2 2F1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 10\nMines: 3\n  0123456789\n0 X2XXX1     0\n1 X311X1     1\n2 2F1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 20\nMines: 3\n  0123456789\n0 X2 1X1     0\n1 X311X1     1\n2 2F1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 30\nMines: 3\n  0123456789\n0 X2 1X1     0\n1 X311X1     1\n2 2F1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nEnter your move (for help enter \"H\"): 41\nMines: 3\n  0123456789\n0 X2 1X1     0\n1 X31111     1\n2 2F1111     2\n3 1111F21    3\n4  1122F1    4\n5  1F22221   5\n6  13F21F1   6\n7   2F2111   7\n8   111      8\n9            9\n  0123456789\nWell done! You solved the board!"
                }
            ],
            "setup": ">>> from input import *\n>>> from main import *\n",
            "type": "doctest"
        }
    ]
}