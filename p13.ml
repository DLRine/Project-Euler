let r =
  let s = ref 0 in
  let f = open_in "p13.txt" in
  for i = 0 to 99 do
    let line = input_line f in
    s := !s + int_of_string (String.sub line 0 13)
  done;
  close_in f;
  !s / 1000
(* max : 99999.... k times -> 100*n < 10**40 <=> 900 S 10**i < 10**40 <=> S < 10**40/900 <=> 10**k-1 < 10**40 <=> 10**k  k < 38*)