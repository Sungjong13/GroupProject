// function get_coordinate() {
//   fetch("http://ip-api.com/json")
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error("get ip url error");
//       }
//       return response.text();
//     })
//     .then((data) => {
//       var lat = data.lat;
//       var lon = data.lon;
//       return [lat, lon];
//     });
// }

// // 망한 async function
// !async function get_coordinate() {
//     var url = "http://ip-api.com/json";

//     let position = await fetch(url)
//       .then((response) => {
//         if (!response.ok) {
//           throw new Error("get ip url error");
//         }
//         return response.json();
//       })
//       .then((data) => {
//         console.log(data)
//         var lat = data.lat;
//         var lon = data.lon;
//         console.log(lat, lon);
//         return [lat, lon];
//       })
//       .catch(error => {
//         console.error(error);
//       });
//     return position;
//   }();

//geocoder backup
// 주소-좌표 변환 객체를 생성합니다
//var geocoder = new kakao.maps.services.Geocoder();
// 주소로 좌표를 검색합니다
//geocoder.addressSearch('{{address}}', function(result, status) {
// 정상적으로 검색이 완료됐으면
//if (status === kakao.maps.services.Status.OK) {
// 맵 생성
//showmap(33.450701,126.570667);
//var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
// 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
//map.setCenter(coords);
//} else {
// 주소 인식 안되면 사용자위치로 map 생성
//alert("카카오 서비스가 주소를 인식하지 못했습니다.");
//currentposmap();
//}
//});
// 기입 받은 address 없을 때
