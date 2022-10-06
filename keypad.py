from more_itertools import locate

def solution(numbers, hand):
    answer = ''
    left_path=["*"]
    right_path=["#"]
    keypad= [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]

    for idx in numbers:
        
        if idx in [1,4,7]:
            answer+='L'
            left_path.append(idx)
        elif idx in [3,6,9]:
            answer+='R'
            right_path.append(idx)
        else:
            left_pos=[[i,j] for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j]==left_path[-1]]
            right_pos=[[i,j] for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j]==right_path[-1]]
            for_pos=[[i,j] for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j]==idx]

            left_distance=abs(left_pos[0][0]-for_pos[0][0])+abs(left_pos[0][1]-for_pos[0][1])
            right_distance=abs(right_pos[0][0]-for_pos[0][0])+abs(right_pos[0][1]-for_pos[0][1])
            
            if left_distance > right_distance:
                answer+='R'
                right_path.append(idx)
                
            elif left_distance < right_distance:
                answer+='L'
                left_path.append(idx)
            else:
                if hand=="right":
                    answer+='R'
                    right_path.append(idx)
                elif hand=="left":
                    answer+='L'
                    left_path.append(idx)
                    
    return answer




if __name__ == "__main__":
    
    numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand="right"
    
    solution(numbers, hand)
    
#    (0,0)(0,1)(0,2)  1 2 3
#    (1,0)(1,1)(1,2)  4 5 6
#    (2,0)(2,1)(2,2)  7 8 9
#    (3,0)(3,1)(3,2)  * 0 #