let m =
  let t = Array.make_matrix 15 15 0 in
  let f = open_in "p345.txt" in
  for i = 0 to 14 do
    let line = input_line f in
    List.iteri
      (fun j x -> t.(i).(j) <- int_of_string x)
      (String.split_on_char ' ' line |> List.filter (( <> ) ""))
  done;
  close_in f;
  t

let subMatrix m n = let r = Array.make_matrix (Array.length m - 1) (Array.length m.(0) - 1) 0 in for i = 0 to Array.length r - 1
let f m = let h = Hashtbl.create 1000000 in for i = 0 to Array.length m -1 do let 
(* L'idée est de Choisir une valeur et de faire le max en créant une sous matrice et mémorisant les résultats dans le hashtabl *)