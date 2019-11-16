program jacard


write(*,*) 'Dame un real r'
read(*,*) r
write(*,*) 'Dame un real l'
read(*,*) rl
write(*,*) 'Dame un real eta'
read(*,*) eta

open(unit=1,file='jcc.dat',status='old')
open(unit=2,file='eta.dat',status='old')
n=1000
do i=0,1000
	x=float(i)*(1./n)
	write(1,*) x, 1.-(1.-x**r)**rl
	if (x .lt. eta) then
	 write(2,*)x, 0
	else 
	 write(2,*)x, 1
	endif
enddo
end
!real function f(x,r,rl)
!	f=1.-(1.-x**r)**rl
!endfunction
