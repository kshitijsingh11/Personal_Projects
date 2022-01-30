const auth = "563492ad6f917000010000013aa99febf6f948859a92de346aafcf79";
const gallery = document.querySelector('.gallery');
const searchInput = document.querySelector('.search-input');
const form = document.querySelector('.search-form');
const morebtn = document.querySelector('.more');
let pageC = 1;
let pageS = 1;
let fetchLink;
let currentSearch;

let searchValue;


// Event Listener
morebtn.addEventListener("click", loadMore);
searchInput.addEventListener('input',updateInput);

form.addEventListener('submit', (e) =>{
  e.preventDefault();
  currentSearch = searchValue;
  searchPhotos(searchValue);
});

function updateInput(e){
  searchValue = e.target.value;
}

// Function to fetch
async function fetchApi(url){
  const dataFetch = await fetch(url, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      Authorization: auth
    }
  });
  const data = await dataFetch.json();
  return data;
}

// function to generate HTML

function genPic(data){
  data.photos.forEach(photo => {
    const galleryImg = document.createElement('div');
     galleryImg.classList.add('gallery-img');
     galleryImg.innerHTML = `
     <div class="gallery-info">
     <p>${photo.photographer}</p>
     <a href=${photo.src.original}><i class="fas fa-download"></i></a>
     </div>
     <img src=${photo.src.large}></img>
     `;
     gallery.appendChild(galleryImg);
   });
}

async function curatedPhotos(){
  fetchLink = 'https://api.pexels.com/v1/curated?per_page=12&page=1';
  const data = await fetchApi(fetchLink);
  genPic(data);
}

async function searchPhotos(search){
  fetchLink = `https://api.pexels.com/v1/search?query=${search}&per_page=12&pa`;
  clear();
  const data = await fetchApi(fetchLink);
  genPic(data);
  gsap.from('.gallery',{opacity:0,duration:1,y:-20,stagger:0.6});

}

function clear(){
  gallery.innerHTML = "";
  searchInput.value = "";
}

async function loadMore(){
  if(currentSearch){
    pageS++;
    fetchLink = `https://api.pexels.com/v1/search?query=${currentSearch}&per_page=15&page=${pageS}`
  }
  else{
    pageC++;
    fetchLink = `https://api.pexels.com/v1/curated?per_page=15&page=${pageC}`
  }
  const data = await fetchApi(fetchLink);
  genPic(data);

}

gsap.from('.drop',{opacity:0,duration:1,y:-20,stagger:0.6});
gsap.from('.gallery',{opacity:0,duration:1,y:-20,stagger:0.6});

curatedPhotos();

