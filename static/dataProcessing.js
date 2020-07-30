function dataProcessing(json_obj,target_dates){
    var dataset = new Array();

    for (i = 0; i < json_obj.length; i++) {
        var news_quantity_temp = [];
        var news_date_temp = []
        for (j = 0; j < json_obj[i]['stats'].length; j++) {
            var temp = json_obj[i]['stats'][j];
            if (target_dates.includes(temp[0])) {
                news_date_temp.push(temp[0])
                news_quantity_temp.push(temp[1]);
            }
        }
        // console.log(news_date_temp)
        // console.log(news_quantity_temp)

        var news_quantity = [];
        var news_date = [];
        for (j = 0; j < target_dates.length; j++) {
            var current_date = target_dates[j];
            news_date.push(current_date)
            if (news_date_temp.includes(current_date)) {
                var index = news_date_temp.indexOf(current_date)
                news_quantity.push(news_quantity_temp[index])
            } else {
                news_quantity.push(0)
            }
        }
        // construct data object
        var data = {}
        data.site = json_obj[i]['site']
        for (var j = 0; j < news_date.length; j++) {
            data[news_date[j]] = news_quantity[j]
        }
        dataset.push(data)
    }

    return dataset;
}