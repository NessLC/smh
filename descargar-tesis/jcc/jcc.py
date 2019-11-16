#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jcc.py
#  
#  Copyright 2019 Ness <ness@Baltazar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
    n=1000
    rf=3
    lf=100
    r=1    
    while(r<=rf):
     l=1
     print(r)
     while(l<=lf):
      nombre='jcc_r'+str(r)+'_l'+str(l)+'.dat'
      print(nombre)
     
      f= open(nombre,"w+")
      for i in range(n):
       x=i/n
       f.write("%f %f\n"% (x,1.-(1.-x**r)**l))
      l=l+10
      f.close()
     r=r+1
     
    	
#		x=float(i)*(1./n)
#	write(1,*) x, 1.-(1.-x**r)**rl
#	if (x .lt. eta) then
#	 write(2,*)x, 0
#	else 
#	 write(2,*)x, 1
#	endif
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
