s='33657;Vogdi, Luora;4685113'

IFS=';' read -ra ADDR <<< $s
for i in "${ADDR[@]}"; do
  echo "$i"
done

echo ${ADDR[0]}
