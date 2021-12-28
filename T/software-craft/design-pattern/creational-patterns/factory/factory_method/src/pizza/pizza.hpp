#pragma once

class Pizza {
public:

  virtual void prepare() = 0;
  virtual void bake() = 0;
  virtual void cut() = 0;
  virtual void box() = 0;
};
