/**
 * get the dates ranging form [startDate, endDate].
 * both bounds are inclusive
 * @param {Date} startDate 
 * @param {Date} endDate 
 */
var getDates = function (startDate, endDate) {
    var dates = [],
        currentDate = startDate,
        addDays = function (days) {
            var date = new Date(this.valueOf());
            date.setDate(date.getDate() + days);
            return date;
        };
    while (currentDate <= endDate) {
        dates.push(currentDate);
        currentDate = addDays.call(currentDate, 1);
    }
    return dates;
};

var dateCounts = 7;
var startDate = new Date(Date.now() - (dateCounts - 1) * 24 * 60 * 60 * 1000);

// Usage
var dates = getDates(startDate, Date.now());
dates.forEach(function (date) {
    console.log(date.toISOString().slice(0, 10));
});