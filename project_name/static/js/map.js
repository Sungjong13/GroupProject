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
