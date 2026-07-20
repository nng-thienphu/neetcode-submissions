class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        usedRoom = []   # mins heap of (end_time, room_number)
        freeRoom = list(range(n))   # mins heap of available room numbers 
        heapq.heapify(freeRoom)
        count = [0] * n 
        meetings.sort() 

        for s, e in meetings: 
            while usedRoom and usedRoom[0][0] <= s: 
                end_time, room = heapq.heappop(usedRoom) 
                heapq.heappush(freeRoom, room)
            
            if freeRoom: 
                room = heapq.heappop(freeRoom) 
                heapq.heappush(usedRoom, (e, room)) 
            else: 
                # wait till we have the room from used room at its end time
                end_time, room = heapq.heappop(usedRoom)  
                heapq.heappush(usedRoom, (end_time + (e-s), room)) 
        
            count[room] += 1 
        
        return count.index(max(count))