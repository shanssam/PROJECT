////function showSection(section) {
////    const sections = document.getElementsByClassName('information');
////    for (let i = 0; i < sections.length; i++) {
////        sections[i].style.display = 'none';
////    }
////    const sectionInfo = document.getElementById(`${section}-info`);
////    if (sectionInfo) {
////        sectionInfo.style.display = 'block';
////    }
////}
//document.getElementById('searchForm').addEventListener('submit', function(event) {
//        event.preventDefault();
//        var searchQuery = document.getElementById('searchInput').value;
//
//        // Open Flipkart search results in a new tab
//        window.open('https://www.flipkart.com/search?q=' + searchQuery, '_blank');
//
//        // Open Amazon search results in a new tab
//        window.open('https://www.amazon.com/s?k=' + searchQuery, '_blank');
//    });