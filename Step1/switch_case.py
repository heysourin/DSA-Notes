# There is no switch case in python!
# But if-else, dictionary can replace it
# an 'elif' checks every case but switch case checks according to the given argument

# !Switch case in JS:
# let day = "Monday"
# switch (day) {
#   case 'Monday':
#     console.log('Kaam hi kaam');
#     break;
#   case "Tuesday":
#     Console.log( "Olpo kaam");
#     break;
#   default:
#     Console.log( "Relax");
# }

#Python Code:
def GetValues(query):
    d = {1: 'Monday',
         2: 'Tuesday',
         3: 'Wedsnesday'
         }
    return d[query]


n = int(input("Case num dalna zara: "))
print(GetValues(n))

#! Another way: Without function

d = {1: 'Jan',
     2: 'Feb',
     3: 'Mar'
     }

m = int(input('Yahan bhi num dalo: '))
print(d[m])
