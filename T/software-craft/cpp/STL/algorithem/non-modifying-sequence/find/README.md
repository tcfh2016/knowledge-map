
## find_if

有个array用来里面存储了元素，最大max=10，但是实际上有些时候比较小。但是在使用的时候之前是直接访问，但现在需要根据满足某种条件访问

```
typedef struct {
  int slot
  int value
}Elem;

std::array(Elem, 10) localDb;


Elem& getElem(int slot)
{
  for (e : localDb)
  {
    if (e.slot == slot)
    {
      return e;
    }    
  }
}

Elem e = getElem(slot);
e...

auto e = std::find_if(localDb.begin(), localDb.end(), [slot](Elem& e) { return e.slot == slot})

```
