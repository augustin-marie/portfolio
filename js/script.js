/* Fonctions d'initialisation
----------------------------------------*/
function init(){
    loadPages("./html/home.html")
}

/*  Fonction du chargement des pages
----------------------------------------*/
$("a").click(function (e) { 
    e.preventDefault();

    contentPath = e.target.pathname;

    if(contentPath !== ""){
        loadPages(contentPath)
    }
});


function loadPages(contentPath) {
    $('#container').load(contentPath);
}

/* Initialisation
----------------------------------------*/
init()
