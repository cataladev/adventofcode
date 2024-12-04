import fileinput

filename = "day2\input.txt"

def main():
    reports = []
    for line in fileinput.input(files=filename):
        report = line.split()

        for i, level in enumerate(report):
            report[i] = int(level)
        reports.append(report)

    safeReports = []

    def isSafe(report):
        increasing = None

        for i in range(1, len(report)):
            difference = report[i] - report[i-1]
            if abs(difference) > 3 or abs(difference) < 1:
                return False
            
            if increasing is None:
                if difference > 0:
                    increasing = True
                elif difference < 0:
                    increasing = False
            elif increasing and difference < 0:
                return False
            elif not increasing and difference > 0:
                return False
        return True
    
    def isSafeWithDampener(report):
        for i in range(0, len(report)):
            dampenedReport = report[:i] + report[i+1:]

            if isSafe(dampenedReport):
                return True

        return False
    
    for report in reports:
        if isSafe(report):
            safeReports.append(report)
        elif isSafeWithDampener(report):
            safeReports.append(report)
        
    
    print(len(safeReports))

            

main()