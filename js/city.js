const province_arr = new Array('Aceh', 'Bali', 'Bangka Belitung', 'Banten', 'Bengkulu', 'Daerah Istimewa Yogyakarta', 'Gorontalo', 'Jakarta', 'Jambi', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Kalimantan Barat', 'Kalimantan Selatan', 'Kalimantan Tengah', 'Kalimantan Timur', 'Kalimantan Utara', 'Kepulauan Riau', 'Lampung', 'Maluku Utara', 'Maluku', 'Nusa Tenggara Barat', 'Nusa Tenggara Timur', 'Papua Barat', 'Papua', 'Riau', 'Sulawesi Selatan', 'Sulawesi Tengah', 'Sulawesi Tenggara', 'Sulawesi Utara', 'Sumatra Barat', 'Sumatra Selatan', 'Sumatra Utara');

const c_a = new Array();
c_a[0] = '';
c_a[1] = 'Banda Aceh | Langsa | Lhokseumawe | Sabang | Subulussalam';
c_a[2] = 'Denpasar';
c_a[3] = 'Pangkalpinang';
c_a[4] = 'Cilegon | Serang | Tangerang Selatan | Tangerang';
c_a[5] = 'Bengkulu';
c_a[6] = 'Yogyakarta';
c_a[7] = 'Gorontalo';
c_a[8] = 'Kota Administrasi Jakarta Barat | Kota Administrasi Jakarta Pusat | Kota Administrasi Jakarta Selatan | Kota Administrasi Jakarta Timur | Kota Administrasi Jakarta Utara';
c_a[9] = 'Sungai Penuh | Jambi';
c_a[10] = 'Bandung | Bekasi | Bogor | Cimahi | Cirebon | Depok | Sukabumi | Tasikmalaya | Banjar';
c_a[11] = 'Magelang | Pekalongan | Salatiga | Semarang | Surakarta | Tegal';
c_a[12] = 'Batu | Blitar | Kediri | Madiun | Malang | Mojokerto | Pasuruan | Probolinggo | Surabaya';
c_a[13] = 'Pontianak | Singkawang';
c_a[14] = 'Banjarbaru | Banjarmasin';
c_a[15] = 'Palangkaraya';
c_a[16] = 'Balikpapan | Bontang | Samarinda';
c_a[17] = 'Tarakan';
c_a[18] = 'Batam | Tanjungpinang';
c_a[19] = 'Bandar Lampung | Metro';
c_a[20] = 'Ternate | Tidore Kepulauan';
c_a[21] = 'Ambon | Tual';
c_a[22] = 'Bima | Mataram | Kupang';
c_a[23] = 'Sorong';
c_a[24] = 'Jayapura';
c_a[25] = 'Dumai | Pekanbaru';
c_a[26] = 'Makassar | Palopo | Parepare';
c_a[27] = 'Palu';
c_a[28] = 'Baubau | Kendari';
c_a[29] = 'Bitung | Kotamobagu | Manado | Tomohon';
c_a[30] = 'Bukittinggi | Padang | Padang Panjang | Pariaman | Payakumbuh | Sawahlunto | Solok';
c_a[31] = 'Lubuklinggau | Pagar Alam | Palembang | Prabumulih | Sekayu';
c_a[32] = 'Gunungsitoli | Medan | Padang Sidempuan | Pematangsiantar | Sibolga | Tanjungbalai | Tebing Tinggi';

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