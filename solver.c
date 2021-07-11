#include <stdint.h>

uint64_t collatz(uint64_t n) {
  
  if(n == 0){
  return 0; // FIXME!
  }
  int s = 0;
  
  while (n != 1){
    if(n % 2 == 0){
      	n = n/2;
		s=s+1;
    }
    else{
      if(n <= UINT64_MAX -(2*n)-1){
        n = (3*n)+1;
      	s=s+1;
     }
      else{
       return 0; 
      }
    }
  }
  return s;
}

printf(collatz(9223372036854775809))