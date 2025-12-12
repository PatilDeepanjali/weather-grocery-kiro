async function load(){
const resp = await fetch('data.json');
const j = await resp.json();
const weather = j.weather.slice(0,40);
const times = weather.map(w=>w.dt);
const temps = weather.map(w=>w.temp);
const pops = weather.map(w=>w.pop*100);


const ctx = document.getElementById('tempChart').getContext('2d');
new Chart(ctx, {type:'line', data:{labels:times, datasets:[{label:'Temp (C)', data:temps, yAxisID:'y'},{label:'Precip Probability (%)', data:pops, yAxisID:'y1'}]}, options:{scales:{y:{type:'linear',position:'left'}, y1:{type:'linear',position:'right'}}}});


// trends: pick one keyword
const trends = j.trends.slice(-20);
const tlabels = trends.map(t=>t.date);
const noodle = trends.map(t=>t.metrics.noodles || 0);
const ctx2 = document.getElementById('trendChart').getContext('2d');
new Chart(ctx2, {type:'bar', data:{labels:tlabels, datasets:[{label:'Noodles interest', data:noodle}]}});
}
load();