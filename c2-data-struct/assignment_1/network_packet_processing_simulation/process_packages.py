# python3
import sys
import os
import time


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []
        self.last_finish_time = 0

    def Process(self, request):
        if len(self.finish_time_) == 0:
            time_at_response = max(self.last_finish_time, request.arrival_time)
            self.last_finish_time = time_at_response + request.process_time
            self.finish_time_.append(self.last_finish_time)
            return Response(False, time_at_response)

        self.last_finish_time = self.finish_time_[-1]
        while len(self.finish_time_) > 0 and \
                (self.finish_time_[0] <= request.arrival_time):
                self.finish_time_.pop(0)

        if len(self.finish_time_) < self.size:
            time_at_response = max(self.last_finish_time, request.arrival_time)
            self.last_finish_time = time_at_response + request.process_time
            self.finish_time_.append(self.last_finish_time)
            return Response(False, time_at_response)
        else:
            return Response(True, -1)


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses


def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":

    # Test for single case
    # text_path = os.path.join(os.getcwd(), 'tests/', '01')
    # with open(text_path) as f:
    #     size, count = map(int, f.readline().split())
    #     requests = []
    #     for i in range(count):
    #         arrival_time, process_time = map(int, f.readline().split())
    #         requests.append(Request(arrival_time, process_time))
    # result_path = text_path + '.a'
    # with open(result_path) as f:
    #     cr = list(map(int, f.read().split()))
    # buffer = Buffer(size)
    # responses = ProcessRequests(requests, buffer)
    # r = []
    # for i in range(len(responses)):
    #     r.append(responses[i].start_time)
    # if cr != r:
    #     print('Wrong')
    # else:
    #     print('Passed')

    # Main program
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)
    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)
    PrintResponses(responses)
