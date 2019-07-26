#create quizzes
import random
state_caps = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas' : 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Idiana' : 'Idianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachussets' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnnesota' : 'St. Paul',
    'Mississipi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Colombus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virgina' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne'    
}

#list of key to be randomized
key_lst = list(state_caps.keys())
#the program asks for the number of students
#nb_stdt = int(input('how many students will be taking the test?'))

#for stdt in range(nb_stdt): #finish that loop later
#create a file with all the questions

random.shuffle(key_lst)

#loop1 ask the question
for caps in key_lst:
    #create a mini list of 4 possible answers
    q_lst = [key_lst[caps]]
    ind_a = key_lst.index(caps)
    
    print(ind_a)
    for i in range(0, 3):
        n_ind = random.randint(0, 46)
        if ind_a != n_ind:
            q_lst.append(key_lst[n_ind])
        else:
            q_lst.append(key_lst[[46 - n_ind]]
            
    random.shuffle(q_lst) #prob here
    
    print(f'Whats the capital city of {caps}\n')
    
    for ans in q_lst:
        print(f'{state_caps[ans]}?\n')


#print(key_lst)