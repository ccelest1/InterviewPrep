/*
    query api endpoint for apartment listings data
    1 - '1-bedroom', 0 - 'studio'
    correct data mixup
    
    edge cases: if word 'studio', '1-bedroom' has 'yoga', 'dance', 'art' -> not considered for num_bedrooms value
        line.split(), filtered = line.split.filter((word)=> word >= 'a' && word <='z' || word <= 'A' && word <= 'Z')
        listings = []
        i, j = -1, 0
        while j < line.length() and  i < j:
            if  line[i]>-1 && ()line[i]!=='yoga' || 'dance' || 'art'):
                if line[j] === 'studio':
                    listings.append(0)
                if line[j] === '1-bedroom':
                    listings.append(1)
                
            j+=1
            i+=1
*/

function solution(jsonData) {
    let listings = []
    for(const listing of jsonData){
        if(listing['description']){
            const description_line = listing['description'].split(" ")
            for(let i = 0; i<description_line.length;i++){
                if(
                    description_line[i-1] !== ('yoga' || 'dance' || 'art'
                )){
                     if(description_line[i] === 'studio'){
                        listings.push(0)
                    }
                    if(description_line[i] === '1-bedroom'){
                        listings.push(1)
                    }
                }
            }
        }
    }
    return listings
}

const input1 = [
   {
      "id": "1",
      "agent": "Radulf Katlego",
      "unit": "#3",
      "description": "This luxurious studio apartment is in the heart of downtown.",
      "num_bedrooms": 1
   },
   {
      "id": "2",
      "agent": "Kelemen Konrad",
      "unit": "#36",
      "description": "We have a 1-bedroom available on the third floor.",
      "num_bedrooms": 1
   },
   {
      "id": "3",
      "agent": "Ton Jett",
      "unit": "#12",
      "description": "Beautiful 1-bedroom apartment with nearby yoga studio.",
      "num_bedrooms": 1
   },
   {
      "id": "4",
      "agent": "Fishel Salman",
      "unit": "#13",
      "description": "Beautiful studio with a nearby art studio.",
      "num_bedrooms": 1
   }
]

const test_result1 = solution(input1)
return test_result1
