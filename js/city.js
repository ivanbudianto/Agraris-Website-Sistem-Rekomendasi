const province_arr = new Array('Aceh', 'Bali', 'Banten', 'Bengkulu', 'Daerah Istimewa Yogyakarta', 'Daerah Khusus Ibukota Jakarta', 'Gorontalo', 'Jambi', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Kalimantan Barat', 'Kalimantan Selatan', 'Kalimantan Tengah', 'Kalimantan Timur', 'Kalimantan Utara', 'Kepulauan Bangka Belitung', 'Kepulauan Riau', 'Lampung', 'Maluku', 'Maluku Utara', 'Nusa Tenggara Barat', 'Nusa Tenggara Timur', 'Papua', 'Papua Barat', 'Riau', 'Sulawesi Barat', 'Sulawesi Selatan', 'Sulawesi Tengah', 'Sulawesi Tenggara', 'Sulawesi Utara', 'Sumatra Barat', 'Sumatra Selatan', 'Sumatra Utara');

const c_a = new Array();
c_a[0] = '';
c_a[1] = 'Meulaboh | Singkil | Karang Baru | Bireun | Sigli | Sinabang | Banda Aceh | Langsa | Lhokseumawe | Sabang';
c_a[2] = 'Amlapura | Bangli | Denpasar | Negara | Semarapura | Singaraja | Tabanan';
c_a[3] = 'Cilegon | Ciruas | Pandeglang | Rangkasbitung | Serang | Tangerang | Tangerang Selatan | Tigaraksa';
c_a[4] = 'Bengkulu | Curup | Karang Tinggi';
c_a[5] = 'Bantul | Sleman | Wates | Wonosari | Yogyakarta';
c_a[6] = 'Cakung | Jakarta | Kembangan | Koja | Menteng';
c_a[7] = 'Gorontalo | Limboto | Tilamuta';
c_a[8] = 'Jambi | Kuala | Sengeti | Sungai Penuh | Tungkal';
c_a[9] = 'Bandung | Banjar | Bekasi | Bogor | Ciamis | Cianjur | Cibinong Cimahi | Cirebon | Depok | Indramayu | Kuningan | Majalengka | Ngamprah | Parigi | Purwakarta | Singaparna | Soreang | Subang | Sukabumi | Sumber | Sumedang Utara | Tasikmalaya';
c_a[10] = 'Banjarnegara | Batang | Blora | Boyolali | Brebes | Demak | Jepara | Kajen | Karanganyar | Kebumen | Kendal | Klaten | Kudus | Magelang | Mungkid | Pati | Pekalongan | Pemalang | Purbalingga | Purwodadi | Purwokerto | Purworejo | Rembang | Salatiga | Semarang | Slawi | Sragen | Sukoharjo | Surakarta | Tegal | Temanggung | Ungaran | Wonogiri | Wonosobo';
c_a[11] = 'Bangil | Bangkalan | Banyuwangi | Batu | Blitar | Bojonegoro | Bondowoso | Caruban | Gresik | Jember | Jombang | Kanigoro | Kediri | Kepanjen | Kraksaan | Lamongan | Lumajang | Madiun | Malang | Mojokerto | Mojosari | Nganjuk | Ngasem | Ngawi | Pamekasan | Pasuruan | Ponorogo | Probolinggo | Sampang | Sidoarjo | Situbondo | Sumenep | Surabaya | Trenggalek | Tuban | Tulungagung';
c_a[12] = 'Ketapang | Pontianak | Sanggau | Singkawang | Sintang | Sukadana | Sungai Raya';
c_a[13] = 'Amuntai | Banjarbaru | Banjarmasin | Barabai | Kandangan | Kotabaru | Martapura | Paringin | Pelaihari | Rantau | Tanjung';
c_a[14] = 'Kasongan | Kuala Kurun | Palangka Raya | Pangkalan Bun | Puruk Cahu | Sampit | Sukamara';
c_a[15] = 'Balikpapan | Bontang | Penajam | Samarinda | Sendawar | Tenggarong';
c_a[16] = 'Tarakan';
c_a[17] = 'Manggar | Muntok | Pangkalpinang | Tanjung Pandan';
c_a[18] = 'Ranai | Tanjung Pinang';
c_a[19] = 'Bandar Lampung | Gedong Tataan | Gunung Sugih | Kalianda | Kotabumi | Krui | Liwa | Menggala | Metro | Panaragan Jaya | Pringsewu | Sukadana';
c_a[20] = 'Ambon | Dobo | Namlea | Piru | Tual';
c_a[21] = 'Bobong | Labuha | Ternate | Tobelo';
c_a[22] = 'Bima | Dompu | Mataram | Praya | Selong | Sumbawa Besar | Taliwang | Tanjung';
c_a[23] = 'Atampua | Bajawa | Borong | Ende | Kefamenanu | Kupang | Labuan Bejo | Maumere | Ruteng | Soe | Waibabul |  Waikabubak | Waingapu';
c_a[24] = 'Biak | Enarotali | Jayapura | Merauke | Nabire | Serui | Tanah Merah | Wamena';
c_a[25] = 'Manokwari | Sorong';
c_a[26] = 'Dumai | Pekanbaru';
c_a[27] = 'Mamasa | Mamuju | Polewali';
c_a[28] = 'Balangnipa | Belopa | Benteng | Bontosunggu | Enrekang | Makale | Makassar | Malili | Masamba | Palopo | Pangkajene | Pinrang | Rentepao | Sengkang | Sungguminasa | Turikale | Watampone';
c_a[29] = 'Banawa | Banggai | Buol | Luwuk | Palu | Parigi | Poso | Salakan | Tolitoli';
c_a[30] = 'Kendari | Lasusua | Rumbia | Sawerigadi | Tirawuta | Unaaha';
c_a[31] = 'Airmadidi | Bitung | Boroko | Kotamobagu | Lolak | Manado | Molibagu | Tomohon | Tondano | Tutuyan';
c_a[32] = 'Batusangkar | Bukittinggi | Padang | Padang Panjang | Painan | Pariaman | Payakumbuh | Sawahlunto | Solok';
c_a[33] = 'Baturaja | Indralaya | Kayu Agung | Lahat | Lubuklinggau | Martapura | Muaradua | Pagar Alam | Palembang | Prabumulih | Sekayu';
c_a[34] = 'Binjai | Gunung Tua | Kabanjahe | Kisaran | Medan | Pandan | Panguruan | Panyabungan | Pinang | Rantau Prapat | Raya | Salak | Sibolga | Stabat | Tanjungbalai | Tebing Tinggi | Teluk Dalam';

function print_province(province_id) {
  const option_str = document.getElementById(province_id);
  option_str.length = 0;
	option_str.options[0] = new Option('Select Province','');
	option_str.selectedIndex = 0;
	for (let i = 0; i < province_arr.length; i++) {
		option_str.options[option_str.length] = new Option(province_arr[i], province_arr[i]);
	}
}

function print_city(city_id, city_index) {
  const option_str = document.getElementById(city_id);
	option_str.length = 0;
	option_str.options[0] = new Option('Select City','');
	option_str.selectedIndex = 0;
	const city_arr = c_a[city_index].split('|');
	for (let i = 0; i < city_arr.length; i++) {
		option_str.options[option_str.length] = new Option(city_arr[i], city_arr[i]);
	}
}