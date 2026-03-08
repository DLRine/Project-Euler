let nbdivisors k =
  let c = ref 1 in
  for i = 2 to k do
    if k mod i = 0 then incr c
  done;
  !c

let nbdivisors2 n =
  let s = ref 0 in
  let e = int_of_float (sqrt (float_of_int n)) in
  for i = 1 to e do
    if n mod i = 0 then incr s
  done;
  s := !s * 2;
  if e * e = n then decr s;
  !s

let number k n = n + k

let result =
  let n, k, divs = (ref 1, ref 1, ref 1) in
  while !divs <= 500 do
    incr k;
    n := !n + !k;
    divs := nbdivisors2 !n
  done;
  (!n, !k, !divs)
(* n = (k*(k+1))/2 *)
