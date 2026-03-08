let chain n =
  let rec aux n len =
    if n = 1 then 1
    else if n mod 2 = 0 then 1 + aux (n / 2) (len)
    else 1 + aux ((3 * n) + 1) (len + 1)
  in
  aux n 1

let () =
  assert (chain 2 = 2);
  assert (chain 13 = 10)

let r =
  let maxn, maxlen = (ref 1, ref 1) in
  for i = 2 to 1000000 do
    let l = chain i in
    if l > !maxlen then begin
      maxn := i;
      maxlen := l
    end
  done;
  (!maxn, !maxlen)
