import sys

bitmap="""
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

bitmap_world="""
...................
        *
       * *
      *   *
     *     *
...................
"""

print("enter msg to display with bitmap")
message=input('> ')

print('\n'*5)

for line in bitmap.splitlines():
    mIndex=0
    for i, bit in enumerate(line):
        if bit ==' ':
            print(' ', end='')
        else:
            print(message[mIndex%len(message)], end='')
            mIndex+=1
    print()

print('\n'*5)



