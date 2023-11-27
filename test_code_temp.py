import numpy as nb
import yaml
# with open("baseline.yaml", "r") as fout:
#     params = yaml.load(fout, Loader = yaml.FullLoader)
# print(params)
# print(params["--export_dir"])
apiData = {
   "page": 1,
   "msg": "地址",
   "data": [{
      "id": 1,
      "name": "学校"
   }, {
      "id": 2,
      "name": "公寓"
   }, {
      "id": 3,
      "name": "流动人口社区"
   }],
}
with open("baseline.yaml", "w", encoding='utf-8') as fout:
    yaml.dump(data = apiData, stream = fout, allow_unicode = True)
    param = yaml.load(fout, Loader = yaml.FullLoader)
print(param)
print("1")
print("2")
print("3")
print("4")

   