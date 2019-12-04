import taichi as ti
import numpy as np

@ti.all_archs
def test_from_numpy_2d():
  val = ti.var(ti.i32)

  n = 4
  m = 7

  @ti.layout
  def values():
    ti.root.dense(ti.ij, (n, m)).place(val)

  for i in range(n):
    for j in range(m):
      val[i, j] = i + j * 3

  arr = val.to_numpy()

  assert arr.shape == (4, 7)
  for i in range(n):
    for j in range(m):
      assert arr[i, j] == i + j * 3

@ti.all_archs
def test_to_numpy_2d():
  val = ti.var(ti.i32)

  n = 4
  m = 7

  @ti.layout
  def values():
    ti.root.dense(ti.ij, (n, m)).place(val)

  arr = np.empty(shape=(n, m), dtype=np.int32)

  for i in range(n):
    for j in range(m):
      arr[i, j] = i + j * 3

  val.from_numpy(arr)

  for i in range(n):
    for j in range(m):
      assert val[i, j] == i + j * 3

@ti.all_archs
def test_to_numpy_2d():
  val = ti.var(ti.i32)

  n = 4
  m = 7

  @ti.layout
  def values():
    ti.root.dense(ti.ij, (n, m)).place(val)

  arr = np.empty(shape=(n, m), dtype=np.int32)

  for i in range(n):
    for j in range(m):
      arr[i, j] = i + j * 3

  val.from_numpy(arr)

  for i in range(n):
    for j in range(m):
      assert val[i, j] == i + j * 3

@ti.all_archs
def test_f64():
  val = ti.var(ti.f64)

  n = 4
  m = 7

  @ti.layout
  def values():
    ti.root.dense(ti.ij, (n, m)).place(val)

  for i in range(n):
    for j in range(m):
      val[i, j] = (i + j * 3) * 1e100

  val.from_numpy(val.to_numpy() * 2)

  for i in range(n):
    for j in range(m):
      assert val[i, j] == (i + j * 3) * 2e100

@ti.all_archs
def test_matrix():
  n = 4
  m = 7
  val = ti.Matrix(2, 3, ti.f32, shape=(n, m))

  nparr = np.empty(shape=(n, m, 2, 3))
  for i in range(n):
    for j in range(m):
      for k in range(2):
        for l in range(3):
          nparr[i, j, k, l] = i + j * 2 - k - l * 3

  val.from_numpy(nparr)
  new_nparr = val.to_numpy()
  assert (nparr == new_nparr).all()
