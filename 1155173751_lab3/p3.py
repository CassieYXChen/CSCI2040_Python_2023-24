import pickle


#file = "followers.pydata"
def load_data(file):
  try:
      f = open(file, 'rb')
      result = pickle.load(f)
      f.close()
      # print(result)
      return result
  except FileNotFoundError:
      print("File not found.")
      return {}


def query_following(user_name):
  dict = load_data("followers.pydata")
  following = 0
  for _user, followers in dict.items():
      if user_name in followers:
          following += 1
  return following


def update():
  dict = load_data("followers.pydata")
  del dict["Lorna Carrico"]
  dict["Anne Smelcer"] = ["Christine Phillips", "Charles Mason", "Tim Lathrop"]
  updated_file = "followers-updated.pydata"
  f = open(updated_file, "wb")
  pickle.dump(dict, f)
  f.close()


def get_num_of_followers():
  update()
  updated_dict = load_data("followers-updated.pydata")
  new_dict = {}
  for user, followers in updated_dict.items():
    new_dict[user] = len(followers)
  return new_dict