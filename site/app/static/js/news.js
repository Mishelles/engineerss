// ID последнего загруженного уведомления
var last_post_loaded = 0;

// Функция для скрытия кнопки "Загрузить ещё" в случае небольшого количества уведомлений
function hideOrShowLoadMore(command="default") {
    if (($(".news-panel").length < 10) || (command == "hide")) {
        $("#load-more-news").hide();
    } else {
        $("#load-more-news").show();
    }
}

// Функция создаёт новый блок для отображения очередного уведомления
function createDivForPost(new_object) {
    var short_text = new_object.text.slice(0, 100);
    var new_element = $(`
        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 inner post" id="post${new_object._id}">
            <div class="media">
                <div class="single-post">
                    <img src="${new_object.image_url}" class="img-responsive" alt="${new_object.title}"/>
                    <div class="pst_info">
                        <div class="media-left">
                            <div class="post-date">
                                <h2>20<br/><span>jan</span></h2>
                            </div>
                        </div>
                    </div>
                    <div class="media-body">
                        <div class="single-post-text">
                            <h2><a href="">${new_object.title}</a></h2>
                            <p>${short_text} <a href="/news/${new_object.slug}">Читать продолжение...</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `);
    return new_element;
}

function loadMoreNews() {
    $.ajax({
      url: `/news/loadmore/${last_post_loaded}`,
      dataType: 'json',
      success: function(data) {
            var news = data['news'];
            for (let i = 0; i < news.length; i++) {
                $("#posts-container").append(createDivForPost(news[i]));
                last_post_loaded = news[i]._id;
                if(news.length < 10) {
                    hideOrShowLoadMore("hide")
                } else {
                    hideOrShowLoadMore();
                }
          }
    }
    });
}

$(document).ready(function() {
    loadMoreNews();
    $("a#load-more-news").click(function() {
        loadMoreNews();
        // Прокручиваемся вниз к подгруженному контенту
        $('html, body').animate({
            scrollTop: $(`#post${last_post_loaded}`).offset().top
        }, 1000);
    });

    $("a#filter_tag").click(function() {
        $("#posts-container").empty();
        last_post_loaded = 0;
        if ($(this).text() == "Все") {
            selected_tag = "all";
        } else {
            selected_tag = $(this).text();
        }
        loadMoreNews();
    });
});
