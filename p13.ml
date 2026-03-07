let nbdivisors k =
  let c = ref 1 in
  for i = 2 to k do
    if k mod i = 0 then incr c
  done;
  !c
let number k n = n + k
let result = let n, k = ref 1, ref 1 in while nbdivisors !n < 500 do incr k; n := !n + !k done; !n