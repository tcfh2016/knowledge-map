#include <iostream>
#include <set>
#include <vector>

class Node {
public:
  Node(int value):next(nullptr), data(value) {}

  void addNode(int value) {
    Node *newNode = new Node(value);
    if (next == nullptr) {
      next = newNode;
    } else {
      newNode->next = next;
      next = newNode;
    }
  }

  void print() {
    Node *p = next;
    while (p != nullptr) {
      std::cout <<p->data <<std::endl;
      p = p->next;
    }
  }

  Node *next;
  int data;
};

void remove_duplictes(Node *link_list) {
  if (link_list == nullptr) {
    return;
  }

  std::set<int> nodes;
  Node *previous = nullptr;
  while (link_list != nullptr) {
    if (nodes.end() != nodes.find(link_list->data)) {
      previous->next = link_list->next;
    } else {
      nodes.insert(link_list->data);
      previous = link_list;
    }
    link_list = link_list->next;
  }
}

int main() {
  Node testNode(0);
  testNode.print();
  std::vector<int> test_array = {1,3,5,7,12,1};
  for (auto e : test_array) {
    testNode.addNode(e);
  }
  testNode.print();
  remove_duplictes(testNode.next);
  testNode.print();

  return 0;
}
