// Big Integer String Operations - bistro.js ver 0.86 20141021
// Copyright (C) 2012-2014 Alexei Kourbatov, JavaScripter.net
//
// Based in part on the public-domain BigInt.js library; see http://leemon.com/crypto/BigInt.html

// CONSTANTS:
bi_MAXINT = 9007199254740991
bi_RADIX  = 10000000
bi_RADINV = 1/bi_RADIX
bi_RADSQR = bi_RADIX*bi_RADIX
bi_LRADIX = 1000000000000000
bi_ONE    = [1,0]; 


function repeat(s,n) {var r=''; if (n>3000000) n=0; while(n>0) {if(n&1) r+=s; if(n>>=1) s+=s;} return r;}

function bi_trim0(s) {  // trim leading zeros from an "integer" string s
 while (s.charAt(0)=='0' && s.length>1) s=s.substring(1);
 return s;
}

function vld(s) {
 var i, s = s.toString().replace(/[^\-\d]/g,'');

 if (s.lastIndexOf('-')>0) s='-'+s.replace(/\-/g,'');
 if (!s.match(/[1-9]/)) s='0';
 else {
  if (s.charAt(0)=='0')    s=s.replace(/^0+/,'');
  if (s.substr(0,2)=='-0') s=s.replace(/^\-0+/,'-');
 }
 return s;
}

function sgn(v) { // sign of v
 if (v=='0')           return  0;
 if (v.charAt(0)=='-') return -1;
 return 1;
}

function abv(v) { // absolute value of v 
 if (v.charAt(0)=='-') return v.substring(1);
 return v;
}

function bi_square(x) { //HAC Algorithm 14.16
  var t, uv, xi, b=[], r=[], L=x.length, M=Math.ceil(L/7);
 
  if (x.charAt(0)=='-') {x=abv(x); L--}
  if (L<9 && (t=x*x)<=bi_MAXINT) return t.toString();
 
  for (var i=0,k=L; k>0; i++,k-=7) b[i] = x.substring(k-7,k)-0;
  for (var i=2*M-1; i>=0; i--)     r[i] = 0;
 
  for (var i=0,k=0;i<M;i++) {
   xi = b[i];
   uv = r[k] + xi*xi;
   r[k] = uv % bi_RADIX;
   xi*= 2;
   for (var j=i+1;j<M;j++) {
    uv = r[i+j] + xi*b[j] + Math.floor(bi_RADINV*uv);
    r[i+j] = uv % bi_RADIX;
   }
   r[i+M] = Math.floor(bi_RADINV*uv);
   k+=2;
  }
  for (var i=0;i<r.length;i++) {
   if (r[i]>=bi_RADIX) {r[i+1] += Math.floor(r[i]*bi_RADINV); r[i]=r[i]%bi_RADIX;}
   r[i] = (''+(bi_RADIX+r[i])).substring(1);
  }
  return bi_trim0(r.reverse().join(''));
 }



function bi_pow(x1,x2){ 
 var r='1', v = vld(x1), v2 = vld(x2), s2 = sgn(v2), a2 = abv(v2), len=v.length;
 var n = parseInt(a2,10), d=parseInt(a2.charAt(a2.length-1),10);

 if (s2 == 0 || v == '1' || v == '-1' && d % 2 == 0) return '1'
 if (v =='-1' && d%2 == 1) return '-1'
 if (s2 == -1 && v == '0') return 'Cannot divide by zero.'
 if (s2 == -1 || v == '0') return '0'

 if (a2.length > 6 || len==1 && n > 250000 || len>1 && n*v.length > 210000) return 'This computation would take too long.'

 while (n>0) {
  if (n & 1) r = bi_multiply(r,v);
  if (n>>=1) v = bi_square(v);
 }
 return r;
}


// multiply integer n < 10^14  by "integer" string x

function bi_multiplyInt(n,a) { 
 var n = parseInt(n,10), m = Math.abs(n), sn = (n==0? 0:(m==n?1:-1)); 
 var sx=sgn(a); if(sx==-1) a=abv(a);
 var r=[], b, t, u, L=a.length, hi = Math.floor(m/bi_RADIX), lo = m % bi_RADIX;

 if (m==0 || a==0) return '0';
 if (m==1) {
  if (sn*sx == 1) return a;
  if (sn*sx ==-1) return '-'+a;
 }

 for (var i=1+Math.ceil(L/7); i>=0; i--) r[i]=0;

 if (hi==0) {
  for (var i=0,k=0; k<L; i++,k+=7) {
   t = m*a.substring(L-k-7,L-k);
   r[i] += t % bi_RADIX;
   r[i+1] += Math.floor(bi_RADINV*t);
  }
 }
 else {
  r[r.length] = 0;
  for (var i=0,k=0; k<L; i++,k+=7) {
   b = a.substring(L-k-7,L-k)-0;
   t = lo*b;
   u = hi*b;
   r[i] += t % bi_RADIX;
   r[i+1] += Math.floor(bi_RADINV*t) + u%bi_RADIX;
   r[i+2] += Math.floor(bi_RADINV*u);
  }
 }
 for (var i=0;i<r.length;i++) {
  if (r[i]>=bi_RADIX) {r[i+1] += Math.floor(bi_RADINV*r[i]); r[i]=r[i]%bi_RADIX;}
  r[i] = (''+(bi_RADIX+r[i])).substring(1);
 }
 if (sn*sx == 1) return     bi_trim0(r.reverse().join(''));
 if (sn*sx ==-1) return '-'+bi_trim0(r.reverse().join(''));
 return '0'
}


function bi_multiply(x1,x2) {
 var v1 = vld(x1), s1 = sgn(v1), a1 = abv(v1);
 var v2 = vld(x2), s2 = sgn(v2), a2 = abv(v2);

 if (s1*s2 == 1) return     multiplyAbs(a1,a2);
 if (s1*s2 ==-1) return '-'+multiplyAbs(a1,a2);
 return '0'
}


function multiplyAbs(a1,a2) {
 if (a1==0 || a2==0) return '0';

 var L1=a1.length, M1=Math.ceil(L1/7);
 var L2=a2.length, M2=Math.ceil(L2/7);
 var t, b, b2=[], r=[]  //, b1=[];

 for (var i=0,k=L2; k>0; i++,k-=7)  b2[i] = a2.substring(k-7,k)-0;
 for (var i=M1+M2-1; i>=0; i--)     r[i]  = 0;

 for (var j=0,k=L1; k>0; j++,k-=7) {
  b = a1.substring(k-7,k)-0; 
  i = j+1;
  for (var l=0;l<M2;l++) {
   t = b*b2[l];
   r[j+l] += t % bi_RADIX;
   r[i+l] += Math.floor(bi_RADINV*t);
  }
 }

 for (var i=0;i<r.length;i++) {
  if (r[i]>=bi_RADIX) {r[i+1] += Math.floor(r[i]*bi_RADINV); r[i]=r[i]%bi_RADIX;}
  r[i] = (''+(bi_RADIX+r[i])).substring(1);
 }
 return bi_trim0(r.reverse().join(''));
}



