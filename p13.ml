let nbdivisors k =
  let c = ref 1 in
  for i = 2 to k do
    if k mod i = 0 then incr c
  done;
  !c