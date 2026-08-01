import os

latex_bab3 = r"""\chapter[METODOLOGI PENELITIAN]{\\ METODOLOGI PENELITIAN}

\section{Tempat dan Waktu Penelitian}
Penelitian ini dilaksanakan di PT PLN (Persero) Unit Induk Distribusi (UID) Aceh yang beralamat di Jalan T. Tjhik Ditiro No. 5, Peuniti, Kecamatan Baiturrahman, Kota Banda Aceh, Aceh. Waktu pelaksanaan penelitian berlangsung selama lima bulan, terhitung mulai bulan Februari hingga bulan Juni 2026.

\section{Alat dan Bahan Penelitian}
Penelitian ini menggunakan beberapa perangkat lunak dan perangkat keras untuk mendukung seluruh tahapan penelitian, mulai dari proses pengumpulan data, pengolahan dan pembersihan data (\textit{preprocessing}), implementasi algoritma K-Means Clustering, hingga pengembangan dan pengujian sistem GridEval PLN. Perangkat lunak yang digunakan mencakup sistem operasi, bahasa pemrograman, serta berbagai \textit{library} dan \textit{framework} yang mendukung proses analisis data dan pembangunan aplikasi berbasis web. Sementara itu, perangkat keras yang digunakan berupa perangkat komputer dengan spesifikasi tertentu yang memadai untuk menjalankan proses pengolahan data dan pengujian sistem secara optimal. Rincian perangkat lunak dan perangkat keras yang digunakan dalam penelitian ini dijelaskan pada sub-bagian berikut.

\subsection{Perangkat Lunak}
Perangkat lunak yang digunakan dalam penelitian ini disajikan pada Tabel 3.1.

\begin{table}[H]
\setstretch{1.2}
\centering
\caption{Kebutuhan Perangkat Lunak}
\label{tab:kebutuhan_perangkat_lunak}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{4cm}|X|}
\hline
\multicolumn{1}{|c|}{\textbf{Perangkat Lunak}} & \multicolumn{1}{c|}{\textbf{Fungsi}} \\ \hline
Windows 11 & Sistem operasi yang digunakan untuk menjalankan aplikasi dan lingkungan pengembangan sistem. \\ \hline
Python 3.12.6 & Bahasa pemrograman yang digunakan untuk pengolahan data dan implementasi algoritma K-Means Clustering. \\ \hline
Pandas 2.3.0 & Library Python yang digunakan untuk manipulasi dan pengolahan data. \\ \hline
NumPy 1.26.4 & Library Python yang digunakan untuk komputasi numerik dan pengolahan data multidimensi. \\ \hline
Scikit-learn & Library Python yang digunakan untuk implementasi algoritma K-Means dan evaluasi hasil clustering. \\ \hline
Flask & Framework web yang digunakan untuk membangun aplikasi berbasis web. \\ \hline
MySQL 8.0.30 & Sistem manajemen basis data yang digunakan untuk penyimpanan data. \\ \hline
Figma & Digunakan untuk merancang wireframe antarmuka sistem. \\ \hline
\end{tabularx}
\end{table}

\subsection{Perangkat Keras}
Perangkat keras yang digunakan dalam penelitian ini disajikan pada Tabel 3.2.

\begin{table}[H]
\setstretch{1.2}
\centering
\caption{Kebutuhan Perangkat Keras}
\label{tab:kebutuhan_perangkat_keras}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{4cm}|X|}
\hline
\multicolumn{1}{|c|}{\textbf{Komponen}} & \multicolumn{1}{c|}{\textbf{Spesifikasi}} \\ \hline
Processor & AMD Ryzen 7 atau setara \\ \hline
RAM & Minimal 8GB \\ \hline
SSD & Minimal 256GB \\ \hline
\end{tabularx}
\end{table}

\section{Variabel Data}
Variabel yang digunakan dalam penelitian ini meliputi:
\begin{enumerate}
\item \textbf{Lama Padam (Jam)}, yaitu durasi waktu sejak terjadinya gangguan hingga sistem kembali normal. Variabel ini digunakan untuk menggambarkan lamanya pemadaman yang dialami pelanggan akibat gangguan listrik.
\item \textbf{Jumlah Pelanggan Padam}, yaitu banyaknya pelanggan yang terdampak akibat gangguan listrik yang terjadi. Variabel ini digunakan untuk menggambarkan luas dampak gangguan terhadap pelanggan.
\item \textbf{Energy Not Supplied (ENS)}, yaitu jumlah energi listrik yang tidak tersalurkan akibat terjadinya gangguan. Variabel ini merepresentasikan besarnya dampak gangguan terhadap sistem secara teknis dan operasional.
\end{enumerate}
Ketiga variabel tersebut digunakan sebagai atribut dalam proses K-Means Clustering untuk mengelompokkan data gangguan listrik berdasarkan karakteristik durasi pemadaman, jumlah pelanggan terdampak, dan nilai ENS. Hasil pengelompokan digunakan untuk mengidentifikasi kelompok gangguan dengan tingkat dampak yang berbeda sehingga dapat menjadi bahan pendukung dalam proses evaluasi data historis gangguan listrik.

\section{Sumber Data}
Data yang digunakan dalam penelitian ini merupakan data sekunder yang diperoleh dari PT PLN (Persero) Unit Induk Distribusi (UID) Aceh. Data tersebut berkaitan dengan gangguan/pemadaman listrik yang terjadi pada wilayah kerja PT PLN (Persero) UID Aceh, yang meliputi variabel jumlah pelanggan padam, lama padam, dan Energy Not Supplied (ENS). Data yang diberikan oleh pihak PLN mencakup periode dua tahun terakhir sebelum data tersebut diserahkan kepada peneliti, dengan format berkas berupa Microsoft Excel (.xlsx).

Teknik pengumpulan data dalam penelitian ini dilakukan melalui beberapa tahapan sebagai berikut:
\begin{enumerate}
\item \textbf{Observasi} \\
Observasi dilakukan untuk memahami proses pencatatan, penyimpanan, dan pengelolaan data gangguan listrik yang digunakan sebagai sumber data penelitian di lingkungan PT PLN (Persero) UID Aceh. Observasi ini bertujuan untuk mengetahui struktur data yang tersedia serta kesesuaian data dengan kebutuhan penelitian.
\item \textbf{Permohonan Data Secara Resmi} \\
Pengumpulan data diawali dengan pengajuan surat permohonan data resmi dari pihak kampus kepada PT PLN (Persero) UID Aceh. Setelah surat tersebut diterima, pihak PLN mengarahkan peneliti untuk mengisi formulir permintaan data (Google Form) sebagai syarat administratif lanjutan untuk memperoleh izin akses data.
\item \textbf{Dokumentasi} \\
Data yang telah disetujui kemudian diperoleh dalam bentuk dokumentasi data historis gangguan listrik yang telah terdigitalisasi dan disimpan oleh pihak PLN. Data tersebut selanjutnya digunakan sebagai bahan analisis dalam penelitian ini.
\end{enumerate}

\section{Tahap Penelitian}
Penelitian ini dilakukan secara sistematis melalui beberapa tahapan yang saling berkaitan, mulai dari proses pengumpulan data hingga pengujian sistem yang dikembangkan. Setiap tahapan disusun secara berurutan agar hasil dari satu tahap dapat digunakan sebagai dasar bagi tahap berikutnya, sehingga proses penelitian dapat berjalan secara terstruktur dan menghasilkan luaran yang sesuai dengan tujuan penelitian. Tahapan penelitian yang dilakukan dalam penyusunan skripsi ini ditampilkan pada Gambar 3.1 berikut.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{tahapan_penelitian}
\caption{Tahapan Penelitian}
\label{fig:tahapan_penelitian}
\end{figure}

Berdasarkan Gambar 3.1, tahapan penelitian tersebut dapat dijelaskan sebagai berikut:

\subsection{Pengumpulan Data}
Tahap ini merupakan proses memperoleh data sekunder gangguan listrik dari PT PLN (Persero) UID Aceh, sebagaimana telah dijelaskan pada sub-bab 3.4 Sumber Data.

\subsection{Preprocessing Data}
Tahap preprocessing dilakukan untuk mempersiapkan data sebelum digunakan pada proses clustering. Tahap ini terdiri atas tiga bagian, yaitu pembersihan data, deteksi outlier, dan normalisasi data.

Pembersihan data (\textit{data cleaning}) dilakukan melalui tiga langkah, yaitu pengecekan dan penanganan nilai kosong (\textit{missing value}) pada variabel JUMLAH\_PELANGGAN, LAMA\_PADAM\_JAM, dan ENS; pengecekan dan penghapusan data duplikat; serta validasi nilai logis dengan memastikan tidak terdapat nilai negatif pada ketiga variabel tersebut, mengingat secara konsep ketiganya tidak mungkin bernilai negatif.

Selanjutnya, dilakukan deteksi nilai ekstrem (\textit{outlier}) pada masing-masing variabel menggunakan metode Interquartile Range (IQR). Metode ini menentukan batas kewajaran data berdasarkan nilai kuartil pertama ($Q_1$), kuartil ketiga ($Q_3$), dan rentang interkuartil ($\text{IQR} = Q_3 - Q_1$), dengan batas bawah sebesar $Q_1 - 1,5 \times \text{IQR}$ dan batas atas sebesar $Q_3 + 1,5 \times \text{IQR}$. Data yang berada di luar rentang tersebut dikategorikan sebagai outlier. Namun, pada penelitian ini nilai outlier yang terdeteksi tidak dihapus dari dataset, melainkan tetap dipertahankan. Hal ini didasarkan pada pertimbangan bahwa nilai ekstrem tersebut bukan merupakan kesalahan pencatatan, melainkan merepresentasikan kejadian gangguan listrik yang benar-benar terjadi di lapangan dengan tingkat dampak yang tinggi, sehingga penting untuk tetap diikutsertakan dalam proses clustering.

Tahap terakhir dari preprocessing adalah normalisasi data menggunakan metode StandardScaler. Normalisasi ini bertujuan untuk menyamakan skala antar variabel penelitian, mengingat rentang nilai antar variabel yang digunakan sangat bervariasi. Proses normalisasi dilakukan dengan mentransformasikan setiap nilai variabel sehingga memiliki rata-rata sama dengan 0 dan standar deviasi sama dengan 1, sehingga setiap variabel memiliki kontribusi yang seimbang dalam proses pembentukan cluster dan tidak didominasi oleh variabel dengan skala nilai yang lebih besar.

\subsection{Model K-Means Clustering}
Sebelum proses clustering dijalankan, terlebih dahulu ditentukan jumlah cluster ($k$) yang optimal dengan mengombinasikan dua metode, yaitu Elbow Method dan Silhouette Score. Pengujian dilakukan terhadap beberapa kemungkinan nilai $k$ dengan menjalankan algoritma K-Means pada setiap nilai $k$ yang diuji, menggunakan metode inisialisasi k-means++ dan jumlah inisialisasi ($n\_init$) sebanyak 10 untuk menjaga kestabilan hasil.

Pada Elbow Method, dihitung nilai inertia (\textit{Sum of Squared Error}) untuk setiap nilai $k$ yang diuji. Nilai inertia akan terus menurun seiring bertambahnya jumlah cluster, namun laju penurunan tersebut akan melambat pada titik tertentu yang membentuk pola siku (\textit{elbow point}). Titik ini mengindikasikan jumlah cluster yang cukup optimal, karena penambahan cluster setelahnya tidak lagi memberikan penurunan inertia yang signifikan. Untuk memvalidasi titik siku yang diperoleh, digunakan pula Silhouette Score pada rentang nilai $k$ yang sama. Silhouette Score mengukur seberapa baik suatu data ditempatkan pada clusternya dibandingkan dengan cluster terdekat lainnya, dengan mempertimbangkan tingkat kohesi (kedekatan data dengan anggota cluster yang sama) dan tingkat separasi (jarak data terhadap cluster terdekat lainnya). Nilai Silhouette Score berkisar antara -1 hingga 1, dengan nilai yang semakin mendekati 1 menunjukkan kualitas pemisahan antar cluster yang semakin baik. Jumlah cluster yang dipilih untuk digunakan pada tahap selanjutnya adalah nilai $k$ yang berada pada titik siku hasil Elbow Method dan sekaligus menghasilkan Silhouette Score tertinggi dibandingkan nilai $k$ lainnya, sehingga penentuan jumlah cluster tidak hanya didasarkan pada satu metode saja, melainkan pada kesesuaian antara kedua metode tersebut.

Setelah jumlah cluster optimal diperoleh, proses clustering dilanjutkan menggunakan algoritma K-Means. Algoritma ini bekerja dengan mengelompokkan data ke dalam sejumlah cluster berdasarkan tingkat kemiripan karakteristik antar data, sehingga data dengan karakteristik serupa akan berada pada cluster yang sama. Proses K-Means dijalankan dengan metode inisialisasi k-means++ untuk penentuan titik pusat (\textit{centroid}) awal, jumlah inisialisasi ($n\_init$) sebanyak 10 kali agar diperoleh hasil pengelompokan yang stabil, serta iterasi maksimum ($max\_iter$) sebanyak 300 kali. Algoritma bekerja secara iteratif dengan menghitung jarak Euclidean antara setiap data dengan centroid masing-masing cluster, mengelompokkan data ke centroid terdekat, kemudian memperbarui posisi centroid berdasarkan rata-rata data anggotanya. Proses ini diulang hingga posisi centroid tidak lagi mengalami perubahan yang signifikan atau telah mencapai kondisi konvergen.

Hasil dari proses clustering berupa sejumlah kelompok data gangguan listrik yang memiliki karakteristik serupa berdasarkan variabel jumlah pelanggan padam, lama padam, dan ENS. Untuk mempermudah interpretasi, setiap cluster yang terbentuk selanjutnya diberi label kategori tingkat dampak berdasarkan peringkat rata-rata nilai centroid pada skala data yang telah dinormalisasi, sehingga setiap cluster dapat merepresentasikan tingkat keparahan gangguan listrik secara relatif satu sama lain.

\subsection{Evaluasi Hasil Clustering}
Tahap terakhir dalam penerapan metode K-Means Clustering adalah evaluasi hasil clustering. Evaluasi ini dilakukan untuk mengetahui kualitas pengelompokan yang dihasilkan, yaitu seberapa baik data pada masing-masing cluster terpisah satu sama lain dan seberapa homogen data di dalam satu cluster yang sama.

Pada penelitian ini, evaluasi hasil clustering dilakukan menggunakan metrik Silhouette Score. Metrik ini dipilih karena mampu mengukur kualitas cluster tanpa memerlukan label kelas yang sebenarnya (\textit{unsupervised evaluation}), sehingga sesuai dengan karakteristik data penelitian yang tidak memiliki label \textit{ground truth}. Silhouette Score mengukur seberapa baik suatu data ditempatkan pada clusternya dibandingkan dengan cluster terdekat lainnya, dengan mempertimbangkan dua komponen, yaitu jarak rata-rata antar data dalam satu cluster yang sama (kohesi) dan jarak rata-rata data tersebut terhadap data pada cluster terdekat (separasi). Nilai Silhouette Score berada pada rentang -1 hingga 1, di mana nilai yang semakin mendekati 1 menunjukkan bahwa cluster yang terbentuk memiliki tingkat kohesi internal yang tinggi sekaligus tingkat pemisahan antar cluster yang baik.

Berdasarkan hasil pengujian, model K-Means final dengan jumlah cluster K=3 menghasilkan nilai Silhouette Score sebesar 0,6012. Nilai ini menunjukkan bahwa kualitas pengelompokan yang dihasilkan tergolong baik, karena berada cukup jauh di atas nilai 0 (yang mengindikasikan tumpang tindih antar cluster) dan cukup mendekati nilai maksimum 1. Dengan demikian, dapat disimpulkan bahwa ketiga cluster yang terbentuk pada penelitian ini, yaitu kategori Dampak Tinggi, Dampak Sedang, dan Dampak Rendah, memiliki tingkat keterpisahan yang cukup jelas dan merepresentasikan pengelompokan data gangguan listrik yang cukup baik berdasarkan variabel lama padam, jumlah pelanggan padam, dan ENS.

\subsection{Rancangan Sistem}
Rancangan sistem pada penelitian ini bertujuan untuk membangun sistem analitik yang mampu mengolah data historis gangguan listrik menggunakan metode K-Means Clustering guna menghasilkan segmentasi kinerja penanganan gangguan. Sistem yang dirancang berfungsi sebagai alat bantu evaluasi berbasis data dan divisualisasikan dalam bentuk dashboard.

\subsubsection{Analisis Kebutuhan Sistem}
Analisis kebutuhan sistem dilakukan untuk mengidentifikasi fitur dan karakteristik yang harus dimiliki oleh sistem agar dapat mendukung proses pengelompokan data gangguan listrik menggunakan metode K-Means Clustering secara optimal. Kebutuhan sistem pada penelitian ini dibagi menjadi dua kategori, yaitu kebutuhan fungsional dan kebutuhan non-fungsional. Kebutuhan fungsional menjelaskan fitur-fitur yang harus disediakan oleh sistem untuk menjalankan proses bisnisnya, mulai dari autentikasi pengguna, pengelolaan data dan akun, penerapan algoritma K-Means Clustering, hingga penyajikan hasil analisis kepada pengguna, sedangkan kebutuhan non-fungsional menjelaskan kualitas dan batasan yang harus dipenuhi oleh sistem dalam menjalankan setiap fungsinya, seperti kemudahan penggunaan, kinerja, keamanan, keandalan, kompatibilitas, kemudahan pemeliharaan, dan ketersediaan sistem. Kebutuhan fungsional sistem ini dijabarkan pada Tabel 3.3, sedangkan kebutuhan non-fungsional sistem dijabarkan pada Tabel 3.4.

\begin{enumerate}
\item \textbf{Kebutuhan Fungsional Sistem}

\begin{table}[H]
\setstretch{1.2}
\centering
\caption{Kebutuhan Fungsional Sistem}
\label{tab:kebutuhan_fungsional}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{4.5cm}|X|}
\hline
\multicolumn{1}{|c|}{\textbf{Kebutuhan Fungsional}} & \multicolumn{1}{c|}{\textbf{Deskripsi}} \\ \hline
Login & Sistem menyediakan halaman login untuk memastikan hanya pengguna yang memiliki akun dapat mengakses sistem. \\ \hline
Kelola Akun & Admin dapat menambahkan, mengubah, menonaktifkan, dan mengatur akun pegawai yang dapat mengakses sistem. \\ \hline
Upload Data Gangguan & Sistem dapat menerima unggahan data historis gangguan listrik dalam format yang telah ditentukan sebagai input analisis. \\ \hline
Validasi Data & Sistem melakukan pemeriksaan terhadap data yang diunggah untuk memastikan format dan struktur data sesuai kebutuhan analisis. \\ \hline
Preprocessing Data & Sistem melakukan pembersihan data dan normalisasi agar data siap digunakan pada proses clustering. \\ \hline
Proses K-Means Clustering & Sistem menerapkan algoritma K-Means untuk mengelompokkan data gangguan berdasarkan karakteristik yang dimiliki. \\ \hline
Evaluasi Hasil Clustering & Sistem menghitung kualitas cluster menggunakan metrik evaluasi seperti Silhouette Score. \\ \hline
Visualisasi Hasil Clustering & Sistem menampilkan hasil pengelompokan dalam bentuk tabel, grafik, dan informasi cluster untuk memudahkan analisis. \\ \hline
Statistik Cluster & Sistem menampilkan informasi statistik setiap cluster, seperti jumlah data pada masing-masing cluster dan karakteristiknya. \\ \hline
Analisis Tren Gangguan & Sistem menampilkan tren gangguan berdasarkan periode waktu tertentu untuk membantu identifikasi pola gangguan. \\ \hline
Export Hasil Analisis & Sistem dapat mengekspor hasil clustering dan hasil analisis ke dalam format file yang tersedia untuk keperluan dokumentasi dan pelaporan. \\ \hline
Logout & Sistem menyediakan fungsi logout untuk mengakhiri sesi penggunaan dan menjaga keamanan akses sistem. \\ \hline
\end{tabularx}
\end{table}

Berdasarkan Tabel 3.3, kebutuhan fungsional sistem terdiri atas sebelas fungsi utama yang mencakup keseluruhan alur kerja sistem, mulai dari proses autentikasi pengguna, pengelolaan data gangguan listrik, penerapan metode K-Means Clustering, hingga penyajian hasil analisis kepada pengguna. Fungsi Login, Kelola Akun, dan Logout disediakan untuk mendukung aspek keamanan dan pengelolaan hak akses pengguna terhadap sistem. Fungsi Upload Data Gangguan, Validasi Data, dan Preprocessing Data digunakan untuk memastikan data yang akan diproses telah sesuai format dan siap digunakan pada tahap clustering. Selanjutnya, fungsi Proses K-Means Clustering dan Evaluasi Hasil Clustering merupakan inti dari sistem, yang masing-masing digunakan untuk mengelompokkan data gangguan listrik dan menilai kualitas cluster yang dihasilkan melalui Silhouette Score. Adapun fungsi Visualisasi Hasil Clustering, Statistik Cluster, dan Analisis Tren Gangguan disediakan untuk membantu pengguna dalam menginterpretasikan hasil pengelompokan secara lebih mudah, sementara fungsi Export Hasil Analisis digunakan untuk mendukung kebutuhan dokumentasi dan pelaporan hasil analisis.

\item \textbf{Kebutuhan Non-Fungsional}

Adapun kebutuhan non-fungsional merupakan aspek yang menjelaskan kualitas serta batasan yang harus dipenuhi oleh sistem dalam menjalankan setiap fungsi yang telah didefinisikan, meliputi aspek kemudahan penggunaan (\textit{usability}), kinerja sistem (\textit{performance}), keamanan (\textit{security}), keandalan (\textit{reliability}), kompatibilitas (\textit{compatibility}), kemudahan pemeliharaan (\textit{maintainability}), serta ketersediaan sistem (\textit{availability}). Kebutuhan non-fungsional sistem tersebut dijabarkan pada Tabel 3.4.

\begin{table}[H]
\setstretch{1.2}
\centering
\caption{Kebutuhan Non-Fungsional}
\label{tab:kebutuhan_non_fungsional}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{3.5cm}|X|}
\hline
\multicolumn{1}{|c|}{\textbf{Aspek}} & \multicolumn{1}{c|}{\textbf{Kebutuhan Non-Fungsional}} \\ \hline
Usability & Sistem harus memiliki antarmuka yang sederhana dan mudah dipahami sehingga dapat digunakan oleh pegawai maupun admin tanpa memerlukan pelatihan khusus. \\ \hline
Performance & Sistem harus mampu memproses data gangguan listrik yang diunggah serta menjalankan proses K-Means Clustering dalam waktu yang relatif singkat. \\ \hline
Security & Sistem harus membatasi hak akses pengguna sesuai dengan peran (\textit{role}) masing-masing, misalnya hanya admin yang dapat mengakses halaman Kelola Akun Pegawai, serta menyimpan kata sandi pengguna dalam bentuk terenkripsi. \\ \hline
Reliability & Sistem harus dapat berjalan secara stabil dan konsisten dalam menghasilkan output clustering meskipun dijalankan berulang kali dengan data yang sama. \\ \hline
Compatibility & Sistem dapat diakses melalui browser umum seperti Google Chrome, Mozilla Firefox, dan Microsoft Edge tanpa memerlukan instalasi tambahan. \\ \hline
Maintainability & Kode program sistem disusun secara modular agar mudah dikembangkan, diperbaiki, atau ditambahkan fitur baru di kemudian hari. \\ \hline
Availability & Sistem harus dapat diakses kapan saja selama server dalam kondisi aktif, agar pegawai dapat melakukan analisis gangguan listrik sesuai kebutuhan. \\ \hline
\end{tabularx}
\end{table}

Berdasarkan Tabel 3.4, kebutuhan non-fungsional sistem mencakup tujuh aspek utama yang berkaitan dengan kualitas dan keandalan sistem dalam menjalankan fungsinya. Aspek usability memastikan sistem mudah digunakan oleh pengguna tanpa memerlukan pelatihan khusus, sedangkan aspek performance dan reliability memastikan sistem dapat memproses data serta menghasilkan output clustering secara cepat dan konsisten. Aspek security berperan penting dalam menjaga keamanan akses sistem melalui pembatasan hak akses berdasarkan peran pengguna, sementara aspek compatibility, maintainability, dan availability memastikan sistem dapat diakses dengan mudah, mudah dikembangkan di masa mendatang, serta dapat digunakan kapan pun dibutuhkan.
\end{enumerate}

\subsection{Rancangan Arsitektur Sistem}
Arsitektur sistem menggambarkan struktur, komponen, serta alur pengolahan data yang terdapat dalam suatu sistem. Pada penelitian ini, arsitektur sistem menunjukkan proses pengolahan data gangguan listrik mulai dari input data, preprocessing, penerapan metode K-Means Clustering, hingga penyajikan hasil analisis melalui dashboard dan laporan.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{arsitektur_sistem}
\caption{Arsitektur Sistem}
\label{fig:arsitektur_sistem}
\end{figure}

Gambar 3.2 menunjukkan rancangan arsitektur sistem evaluasi penanganan gangguan listrik yang dikembangkan dalam penelitian ini. Arsitektur sistem menggambarkan alur proses pengolahan data mulai dari data gangguan listrik yang diunggah oleh pengguna, kemudian diproses melalui tahapan preprocessing yang meliputi data cleaning dan normalisasi data. Data yang telah diproses selanjutnya dianalisis menggunakan algoritma K-Means Clustering untuk menghasilkan pengelompokan data gangguan berdasarkan karakteristik durasi dan tingkat dampaknya. Hasil clustering kemudian dievaluasi menggunakan metrik kualitas cluster untuk memastikan hasil pengelompokan yang diperoleh memiliki tingkat validitas yang baik. Seluruh hasil analisis disajikan melalui dashboard dalam bentuk informasi statistik, visualisasi hasil clustering, serta analisis tren bulanan yang dapat membantu pengguna dalam memahami pola gangguan listrik. Selain itu, sistem juga menyediakan fitur ekspor hasil analisis untuk mendukung kebutuhan dokumentasi dan pelaporan. Dengan arsitektur ini, proses analisis data gangguan dapat dilakukan secara terintegrasi mulai dari pengolahan data hingga penyajian informasi hasil analisis.

\subsubsection{Use Case Diagram}
Use Case Diagram digunakan untuk menggambarkan interaksi antara pengguna dengan sistem yang dikembangkan, yang menunjukkan fungsi-fungsi utama yang dapat diakses oleh masing-masing pengguna berdasarkan hak akses yang dimilikinya. Pada sistem ini terdapat dua aktor, yaitu Admin dan Pegawai. Admin memiliki hak akses untuk mengelola data gangguan listrik, menjalankan proses analisis clustering, serta mengelola akun pengguna sistem, sedangkan Pegawai hanya memiliki hak akses untuk melihat hasil analisis yang telah dihasilkan oleh sistem tanpa dapat mengelola data maupun menjalankan proses analisis.

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth]{use_case_diagram}
\caption{Use Case Diagram}
\label{fig:use_case_diagram}
\end{figure}

Berdasarkan Gambar 3.3, aktor Admin memiliki hak akses penuh terhadap seluruh fungsi utama sistem, yaitu melakukan login, mengelola akun pegawai, mengunggah data gangguan listrik, menjalankan proses analisis menggunakan metode K-Means Clustering, melihat dashboard visualisasi dan hasil clustering, mengakses fitur analisis tren gangguan, mengekspor laporan hasil analisis, mengubah password akun, serta melakukan logout setelah selesai menggunakan sistem. Sementara itu, aktor Pegawai memiliki hak akses yang lebih terbatas dan berfokus pada pemanfaatan hasil analisis, yaitu melakukan login, melihat dashboard visualisasi, melihat hasil clustering, mengakses fitur analisis tren gangguan, mengubah password akun, serta melakukan logout, tanpa memiliki hak untuk mengunggah data, menjalankan proses clustering, mengelola akun pengguna, maupun mengekspor laporan hasil analisis.

\subsubsection{Activity Diagram}
Activity Diagram digunakan untuk menggambarkan alur kerja dan urutan aktivitas yang terjadi dalam sistem. Diagram ini menunjukkan interaksi antara pengguna dan sistem dalam menjalankan fungsi-fungsi yang tersedia pada aplikasi.

\begin{enumerate}
\item \textbf{Activity Diagram Login} \\
Activity Diagram Login menggambarkan alur proses autentikasi pengguna saat mengakses sistem menggunakan NIP dan password yang telah terdaftar.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{act_login}
\caption{Activity Diagram Login}
\label{fig:act_login}
\end{figure}

Gambar 3.4 Activity Diagram Login menggambarkan alur proses autentikasi pengguna saat mengakses sistem menggunakan NIP dan password yang telah terdaftar. Proses dimulai ketika pengguna membuka halaman login dan memasukkan NIP serta password. Data yang dimasukkan kemudian dikirim ke sistem untuk dilakukan proses validasi. Sistem memeriksa kesesuaian data akun yang tersimpan pada basis data. Apabila data yang dimasukkan valid, sistem akan menampilkan halaman dashboard sesuai hak akses pengguna. Namun apabila data tidak valid, sistem akan menampilkan pesan kesalahan dan pengguna diminta untuk mengulangi proses login dengan memasukkan kembali NIP dan password yang benar.

\item \textbf{Activity Diagram Kelola Akun Pegawai} \\
Activity Diagram Kelola Akun Pegawai menggambarkan proses yang dilakukan Admin dalam mengelola akun pegawai yang dapat mengakses sistem.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{act_kelola_akun}
\caption{Activity Diagram Kelola akun Pegawai}
\label{fig:act_kelola_akun}
\end{figure}

Gambar 3.5 Activity Diagram Kelola Akun Pegawai menggambarkan proses yang dilakukan Admin dalam mengelola akun pegawai yang dapat mengakses sistem. Proses dimulai ketika Admin membuka menu kelola akun, kemudian sistem menampilkan form daftar akun yang tersedia. Admin selanjutnya mengisi data pegawai pada form yang tersedia, setelah itu sistem melakukan validasi terhadap data yang diinputkan. Apabila data yang dimasukkan valid, sistem akan menyimpan data akun ke basis data dan menampilkan notifikasi bahwa proses pengelolaan akun berhasil dilakukan. Apabila data tidak valid, sistem akan menampilkan pesan kesalahan dan Admin diminta untuk memperbaiki data yang diinputkan sebelum menyimpan kembali.

\item \textbf{Activity Diagram Clustering} \\
Activity Diagram Proses Clustering menggambarkan alur pengolahan data gangguan listrik mulai dari proses unggah data hingga menghasilkan hasil pengelompokan menggunakan metode K-Means Clustering.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{act_clustering}
\caption{Activity Diagram Clustering}
\label{fig:act_clustering}
\end{figure}

Gambar 3.6 Activity Diagram Clustering menggambarkan alur pengolahan data gangguan listrik mulai dari proses unggah data hingga menghasilkan hasil pengelompokan menggunakan metode K-Means Clustering. Proses dimulai ketika Admin memilih fitur upload data dan memilih file data gangguan listrik yang akan diunggah. Sistem kemudian melakukan validasi terhadap data yang diunggah untuk memastikan kesesuaian format dengan ketentuan yang berlaku. Apabila data tidak valid, sistem akan menampilkan pesan kesalahan dan Admin diminta untuk mengunggah ulang file data yang sesuai. Apabila data valid, sistem akan melakukan preprocessing yang meliputi pembersihan dan normalisasi data, kemudian menjalankan proses K-Means Clustering untuk mengelompokkan data gangguan berdasarkan karakteristik yang dimiliki. Hasil clustering selanjutnya dievaluasi menggunakan metrik kualitas cluster, disimpan ke dalam basis data, dan ditampilkan pada dashboard sistem.

\item \textbf{Activity Diagram Analisis Tren} \\
Activity Diagram Analisis Tren menggambarkan proses penyajian informasi tren gangguan listrik berdasarkan data yang telah dianalisis oleh sistem.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{act_analisis_tren}
\caption{Activity Diagram Analisis Tren}
\label{fig:act_analisis_tren}
\end{figure}

Gambar 3.7 Activity Diagram Analisis Tren menggambarkan proses penyajian informasi tren gangguan listrik berdasarkan data yang telah tersimpan dalam basis data sistem. Proses dimulai ketika pengguna, baik Admin maupun Pegawai, memilih menu analisis tren. Sistem kemudian mengambil data hasil clustering yang tersimpan pada basis data dan melakukan perhitungan statistik berdasarkan periode bulanan. Hasil pengolahan tersebut selanjutnya disajikan dalam bentuk grafik dan informasi statistik tren yang dapat digunakan untuk mengidentifikasi pola serta tren gangguan listrik dari waktu ke waktu.
\end{enumerate}

\subsubsection{Sequence Diagram}
Sequence Diagram digunakan untuk menggambarkan urutan interaksi atau pertukaran pesan antara objek-objek yang terlibat dalam suatu proses berdasarkan waktu terjadinya. Berbeda dengan Activity Diagram yang berfokus pada alur logika dan pengambilan keputusan dalam suatu proses, Sequence Diagram lebih menekankan pada bagaimana objek-objek tersebut saling berkomunikasi secara berurutan untuk menyelesaikan suatu fungsi tertentu. Pada penelitian ini, Sequence Diagram digunakan untuk menggambarkan interaksi antara Aktor, Sistem, dan Database dalam menjalankan proses login, kelola akun pegawai, clustering, dan analisis tren gangguan listrik.

\begin{enumerate}
\item \textbf{Sequence Diagram Login} \\
Proses login dilakukan untuk memastikan hanya pengguna yang memiliki akun terdaftar yang dapat mengakses sistem. Pada proses ini, Aktor menginput NIP dan password yang kemudian diverifikasi oleh Sistem melalui pengecekan data akun pada Database sebelum pengguna diarahkan ke halaman yang sesuai dengan hak aksesnya.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{seq_login}
\caption{Sequence Diagram Login}
\label{fig:seq_login}
\end{figure}

Gambar 3.8 Sequence Diagram Login menggambarkan urutan interaksi antara Aktor, Sistem, dan Database dalam proses autentikasi pengguna. Proses dimulai ketika Aktor menginput NIP dan password pada halaman login. Sistem kemudian mengirimkan permintaan ke Database untuk mengambil data akun berdasarkan NIP yang dimasukkan. Setelah data akun diterima, Sistem melakukan pemeriksaan terhadap empat kemungkinan kondisi, yaitu apabila akun tidak ditemukan, password tidak sesuai, akun berstatus nonaktif, atau data valid dan akun aktif. Apabila salah satu dari tiga kondisi pertama terpenuhi, Sistem akan mengirimkan pesan kesalahan yang sesuai kepada Aktor. Sebaliknya, apabila data valid dan akun berstatus aktif, Sistem akan menampilkan halaman dashboard sesuai dengan hak akses (\textit{role}) yang dimiliki oleh Aktor.

\item \textbf{Sequence Diagram Kelola Akun} \\
Proses kelola akun pegawai dilakukan oleh Admin untuk mengelola data akun pengguna sistem, mulai dari menambahkan, mengubah, hingga menonaktifkan akun pegawai. Sistem akan memvalidasi data yang diinput sebelum disimpan ke dalam Database.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{seq_kelola_akun}
\caption{Sequence Diagram Kelola Akun}
\label{fig:seq_kelola_akun}
\end{figure}

Gambar 3.9 Sequence Diagram Kelola Akun Pegawai menggambarkan urutan interaksi antara Admin, Sistem, dan Database dalam proses pengelolaan akun pegawai. Proses dimulai ketika Admin membuka menu kelola akun, kemudian Sistem meminta daftar akun yang tersimpan pada Database dan menampilkannya kepada Admin. Selanjutnya, Admin menginput data pegawai yang akan ditambahkan atau diubah, dan Sistem melakukan validasi terhadap format serta keunikan NIP yang dimasukkan. Apabila data tidak valid atau NIP telah terdaftar sebelumnya, Sistem akan mengirimkan pesan kesalahan kepada Admin. Apabila data dinyatakan valid, Sistem akan menyimpan atau memperbarui data akun pada Database, kemudian menerima konfirmasi penyimpanan dan menampilkan notifikasi keberhasilan kepada Admin.

\item \textbf{Sequence Diagram Clustering} \\
Proses clustering dilakukan untuk mengelompokkan data gangguan listrik menggunakan metode K-Means. Admin mengunggah data gangguan yang kemudian divalidasi dan diproses oleh Sistem, dengan hasil akhirnya disimpan ke dalam Database dan ditampilkan pada dashboard.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{seq_clustering}
\caption{Sequence Diagram Clustering}
\label{fig:seq_clustering}
\end{figure}

Gambar 3.10 Sequence Diagram Proses Clustering menggambarkan urutan interaksi antara Admin, Sistem, dan Database dalam proses pengelompokan data gangguan listrik. Proses dimulai ketika Admin mengunggah file data gangguan listrik ke sistem. Sistem selanjutnya melakukan validasi terhadap format dan struktur data yang diunggah. Apabila data tidak valid, Sistem akan mengirimkan pesan kesalahan kepada Admin dan meminta data diunggah ulang. Apabila data valid, Sistem akan menyimpan data mentah ke Database, kemudian menjalankan proses clustering menggunakan algoritma K-Means. Setelah proses clustering selesai, Sistem menyimpan hasil pengelompokan beserta skor evaluasi ke Database, menerima konfirmasi penyimpanan, dan menampilkan hasil clustering pada dashboard yang dapat dilihat oleh Admin.

\item \textbf{Sequence Diagram Analisis Tren} \\
Proses analisis tren dilakukan untuk menampilkan pola gangguan listrik berdasarkan periode waktu tertentu. Pengguna menentukan periode yang ingin dilihat, kemudian Sistem mengambil data hasil clustering dari Database untuk diolah menjadi informasi tren yang ditampilkan kepada pengguna.

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{seq_analisis_tren}
\caption{Sequence Diagram Analisis Tren}
\label{fig:seq_analisis_tren}
\end{figure}

Gambar 3.11 Sequence Diagram Analisis Tren menggambarkan urutan interaksi antara Pengguna, Sistem, dan Database dalam proses penyajian informasi tren gangguan listrik. Proses dimulai ketika Pengguna memilih menu analisis tren dan menentukan periode waktu yang ingin dianalisis. Sistem kemudian memeriksa ketersediaan data hasil clustering pada periode tersebut ke Database. Apabila data tidak tersedia, Sistem akan menampilkan pesan bahwa data belum tersedia untuk periode yang dipilih. Apabila data tersedia, Sistem akan mengambil data hasil cluster dari Database, melakukan perhitungan statistik berdasarkan periode yang ditentukan, kemudian menampilkan hasilnya dalam bentuk grafik dan tabel tren kepada Pengguna.
\end{enumerate}

\subsubsection{Class Diagram}
Class Diagram digunakan untuk menggambarkan struktur statis sistem, yang meliputi kelas-kelas yang terlibat beserta atribut, method (operasi), dan hubungan antar kelas tersebut. Class Diagram pada penelitian ini dirancang berdasarkan hasil analisis kebutuhan sistem, use case diagram, serta activity diagram dan sequence diagram yang telah dibuat sebelumnya.

\begin{figure}[H]
\centering
\includegraphics[width=0.7\textwidth]{class_diagram}
\caption{Class Diagram}
\label{fig:class_diagram}
\end{figure}

Berdasarkan Gambar 3.12, sistem terdiri atas kelas User sebagai kelas induk yang diturunkan menjadi kelas Admin dan Pegawai, dengan pembagian hak akses sesuai peran masing-masing. Kelas DataGangguan merepresentasikan data gangguan listrik yang diunggah oleh Admin, yang kemudian diproses oleh kelas ClusteringEngine untuk menjalankan tahapan preprocessing dan algoritma K-Means Clustering. Hasil dari proses tersebut disimpan pada kelas HasilCluster, yang selanjutnya digunakan oleh kelas AnalisisTren untuk menghasilkan statistik dan grafik tren gangguan berdasarkan periode waktu tertentu. Kelas Admin memiliki relasi langsung dengan kelas DataGangguan dalam mengunggah data, sedangkan kelas Pegawai memiliki relasi dengan kelas HasilCluster dan AnalisisTren untuk melihat hasil analisis yang telah dihasilkan oleh sistem.

\subsection{Perancangan Antarmuka Sistem}
Perancangan antarmuka sistem bertujuan untuk memberikan gambaran mengenai tampilan serta interaksi pengguna dengan sistem yang akan dibangun. Perancangan ini disusun dalam bentuk \textit{wireframe} yang menggambarkan tata letak setiap halaman, penempatan komponen, serta fungsi utama yang tersedia pada masing-masing antarmuka. Wireframe digunakan sebagai acuan dalam proses implementasi sistem agar tampilan yang dikembangkan sesuai dengan kebutuhan pengguna dan fungsionalitas yang telah dirancang.

\subsubsection{Rancangan Halaman Login}
Rancangan Halaman login merupakan halaman awal yang digunakan sebagai proses autentikasi pengguna sebelum mengakses sistem. Halaman ini dirancang dengan tampilan yang sederhana dan mudah dipahami sehingga memudahkan pengguna dalam melakukan proses login. Selain berfungsi sebagai media autentikasi, halaman login juga menampilkan logo aplikasi serta deskripsi singkat mengenai sistem sebagai identitas dan informasi awal bagi pengguna.

\begin{figure}[H]
\centering
\includegraphics[width=0.6\textwidth]{wf_login}
\caption{Wireframe Halaman Login}
\label{fig:wf_login}
\end{figure}

Pada Gambar 3.13, halaman login terdiri atas logo aplikasi, nama aplikasi, deskripsi singkat mengenai fungsi sistem, kolom Username (NIP), kolom Password, serta tombol Login. Pengguna melakukan autentikasi dengan memasukkan NIP sebagai username dan password yang telah terdaftar pada sistem. Setelah data login berhasil divalidasi, sistem akan mengidentifikasi role pengguna. Apabila pengguna memiliki role sebagai Admin, sistem akan mengarahkan ke Dashboard Admin yang memiliki hak akses untuk mengunggah data gangguan listrik, menjalankan proses clustering, mengelola akun pengguna, melihat dashboard, analisis tren, serta mengekspor laporan. Sebaliknya, apabila pengguna memiliki role sebagai Pegawai, sistem akan mengarahkan ke Dashboard Pegawai yang hanya memiliki hak akses untuk melihat dashboard, hasil clustering, analisis tren gangguan, serta mengubah password miliknya sendiri.

\subsubsection{Rancangan Halaman Dashboard Admin}
Dashboard Admin merupakan halaman utama yang ditampilkan setelah Admin berhasil melakukan login. Halaman ini dirancang sebagai pusat navigasi sekaligus panduan awal dalam menggunakan sistem. Pada tampilan awal, dashboard belum menampilkan hasil analisis, melainkan berisi informasi singkat mengenai tahapan penggunaan aplikasi serta petunjuk kepada Admin untuk melakukan proses clustering terhadap data gangguan listrik yang akan dianalisis.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_dashboard_awal}
\caption{Wireframe Halaman Dashboard Admin}
\label{fig:wf_dashboard_awal}
\end{figure}

Pada Gambar 3.14, halaman Dashboard Admin menampilkan logo aplikasi, menu navigasi, deskripsi singkat mengenai fungsi sistem, serta informasi yang mengarahkan Admin untuk memulai proses clustering data gangguan listrik. Pada halaman ini tersedia tombol "Mulai Clustering" yang berfungsi untuk mengarahkan Admin ke halaman clustering. Melalui halaman tersebut, Admin dapat mengunggah data gangguan listrik dan menjalankan proses clustering menggunakan metode K-Means. Setelah proses clustering selesai dilakukan, sistem akan menampilkan hasil analisis berupa dashboard visualisasi, hasil clustering, serta analisis tren gangguan yang dapat digunakan sebagai pendukung proses evaluasi kinerja penanganan gangguan listrik.

Setelah proses clustering selesai dilakukan, tampilan Dashboard Admin akan diperbarui secara otomatis untuk menampilkan ringkasan hasil analisis yang dihasilkan oleh sistem. Informasi yang disajikan dalam dashboard bertujuan untuk memudahkan Admin dalam memantau hasil clustering serta memperoleh gambaran umum mengenai kondisi gangguan listrik berdasarkan data yang telah dianalisis.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_dashboard_clustering}
\caption{Halaman Dashboard Admin (Setelah Proses Clustering)}
\label{fig:wf_dashboard_clustering}
\end{figure}

Pada Gambar 3.15, Dashboard Admin menampilkan ringkasan informasi hasil clustering dalam bentuk visualisasi interaktif. Pada bagian atas halaman ditampilkan informasi mengenai total kejadian pemadaman serta jumlah gangguan pada setiap cluster sebagai ringkasan hasil pengelompokan data. Selanjutnya, sistem menyajikan scatter plot clustering yang menggambarkan persebaran data berdasarkan hasil pengelompokan menggunakan metode K-Means. Selain itu, dashboard juga menampilkan diagram distribusi cluster yang memperlihatkan proporsi data pada masing-masing cluster serta grafik distribusi kejadian gangguan per bulan untuk membantu Admin dalam mengidentifikasi pola gangguan listrik berdasarkan periode waktu tertentu. Seluruh informasi tersebut disajikan secara visual agar memudahkan proses evaluasi dan pengambilan keputusan terhadap penanganan gangguan listrik.

\subsubsection{Rancangan Halaman Clustering Admin}
Halaman clustering merupakan halaman yang digunakan oleh Admin untuk memulai proses analisis data gangguan listrik menggunakan metode K-Means Clustering. Pada halaman ini, sistem memberikan deskripsi singkat serta petunjuk mengenai format dan jenis data yang harus diunggah agar proses clustering dapat berjalan dengan baik. Selain itu, halaman ini juga menyediakan fasilitas untuk mengunggah data serta menampilkan riwayat data yang pernah digunakan dalam proses clustering.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_clustering_sebelum}
\caption{Wireframe Halaman Clustering (Sebelum Upload Data)}
\label{fig:wf_clustering_sebelum}
\end{figure}

Pada Gambar 3.16, halaman clustering menampilkan deskripsi singkat mengenai proses unggah data beserta petunjuk penggunaan sistem sebelum proses clustering dilakukan. Admin dapat mengunggah data gangguan listrik dengan menekan tombol "Pilih Data", kemudian memilih file yang akan digunakan sebagai data masukan dalam proses clustering. Di bagian bawah halaman tersedia tabel Riwayat Unggahan Data yang berfungsi untuk menampilkan daftar file yang telah diunggah sebelumnya. Informasi yang ditampilkan pada tabel meliputi nomor, nama file, jumlah baris data, tanggal unggahan, dan aksi. Melalui kolom aksi, Admin dapat memilih file yang akan digunakan untuk proses clustering berikutnya atau melakukan pengelolaan terhadap data yang telah diunggah sesuai kebutuhan sistem.

Setelah proses clustering selesai dilakukan, sistem akan menyimpan hasil analisis dan menampilkannya pada tabel riwayat clustering. Riwayat ini berfungsi sebagai dokumentasi proses analisis yang telah dilakukan sehingga Admin dapat mengakses kembali hasil clustering tanpa perlu mengunggah ulang dataset yang sama.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_clustering_setelah}
\caption{Wireframe Halaman Clustering (Setelah Upload Data)}
\label{fig:wf_clustering_setelah}
\end{figure}

Pada Gambar 3.17, tabel riwayat clustering menampilkan informasi mengenai dataset yang telah berhasil diproses. Informasi yang ditampilkan meliputi nomor, nama file, jumlah baris data, dan tanggal unggahan. Pada kolom Aksi, tersedia tombol "Lihat Analisis" dan "Hapus". Tombol "Lihat Analisis" digunakan untuk menampilkan kembali hasil clustering beserta visualisasi dan informasi analisis yang telah dihasilkan oleh sistem, sedangkan tombol "Hapus" digunakan untuk menghapus riwayat hasil clustering apabila data tersebut sudah tidak diperlukan lagi.

Setelah proses clustering selesai dilakukan, Admin dapat melihat hasil analisis dengan memilih tombol "Lihat Analisis" pada tabel riwayat analisis clustering. Halaman ini masih berada pada menu clustering, namun sistem akan menampilkan hasil analisis secara lengkap berdasarkan dataset yang dipilih.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_clustering_hasil}
\caption{Wireframe Halaman Clustering (Hasil Clustering)}
\label{fig:wf_clustering_hasil}
\end{figure}

Pada Gambar 3.18, setelah tombol "Lihat Analisis" dipilih, sistem akan menampilkan hasil analisis clustering pada halaman yang sama. Informasi yang disajikan meliputi total data yang berhasil diproses, nilai rata-rata centroid pada setiap cluster, serta grafik distribusi data per cluster untuk memberikan gambaran mengenai persebaran data hasil clustering. Selain itu, sistem juga menampilkan tabel data hasil clustering yang berisi seluruh data beserta label cluster yang dihasilkan oleh algoritma K-Means. Pada bagian bawah tabel tersedia tombol "Download Excel" untuk mengunduh hasil clustering dalam format Microsoft Excel serta tombol "Download PDF" untuk mengunduh laporan hasil analisis dalam format PDF. Fitur tersebut memudahkan Admin dalam mendokumentasikan serta membagikan hasil analisis sesuai kebutuhan.

\subsubsection{Rancangan Halaman Analisis Tren}
Halaman Analisis Tren merupakan halaman yang digunakan untuk menganalisis pola gangguan listrik berdasarkan periode waktu tertentu. Halaman ini dirancang untuk membantu Admin memperoleh informasi mengenai kecenderungan gangguan listrik melalui beberapa pilihan analisis yang tersedia. Sebelum proses analisis dilakukan, Admin dapat menentukan jenis analisis dan periode waktu yang akan digunakan sehingga hasil yang ditampilkan sesuai dengan kebutuhan. Dengan adanya fitur ini, Admin dapat melakukan analisis secara lebih terarah terhadap data gangguan listrik yang telah diproses sebelumnya, sehingga informasi yang dihasilkan dapat digunakan sebagai pendukung dalam proses evaluasi kinerja penanganan gangguan listrik serta membantu pengambilan keputusan berdasarkan tren gangguan yang terjadi.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_analisis_sebelum}
\caption{Wireframe Halaman Analisis (Sebelum Mulai Analisis)}
\label{fig:wf_analisis_sebelum}
\end{figure}

Pada Gambar 3.19, halaman Analisis Tren menampilkan deskripsi singkat mengenai fungsi analisis tren beserta beberapa komponen yang digunakan untuk menentukan parameter analisis. Halaman ini menyediakan fitur Pilih Tipe Analisis yang digunakan untuk menentukan jenis analisis yang akan ditampilkan oleh sistem, serta fitur Pilih Bulan untuk menentukan periode data yang akan dianalisis. Setelah seluruh parameter dipilih, Admin dapat menekan tombol "Mulai Analisis" untuk menjalankan proses analisis tren. Selanjutnya, sistem akan mengolah data sesuai dengan parameter yang dipilih dan menampilkan hasil analisis dalam bentuk visualisasi maupun informasi pendukung pada halaman yang sama.

Setelah Admin menentukan tipe analisis dan periode waktu yang diinginkan, sistem akan memproses data berdasarkan parameter yang telah dipilih. Hasil analisis kemudian ditampilkan pada halaman yang sama dalam bentuk ringkasan informasi, visualisasi data, serta tabel hasil analisis. Penyajikan informasi secara visual bertujuan untuk memudahkan Admin dalam memahami pola gangguan listrik dan karakteristik setiap cluster yang terbentuk.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_analisis_hasil}
\caption{Wireframe Halaman Analisis Tren (Hasil Analisis)}
\label{fig:wf_analisis_hasil}
\end{figure}

Berdasarkan Gambar 3.20, setelah tombol "Mulai Analisis" ditekan, sistem akan menampilkan hasil analisis tren berdasarkan parameter yang telah dipilih. Informasi yang disajikan diawali dengan ringkasan hasil analisis yang meliputi total data, durasi padam rata-rata, total Energy Not Supplied (ENS), serta nilai rata-rata centroid pada setiap cluster. Selanjutnya, sistem menyajikan grafik distribusi data per cluster untuk memperlihatkan proporsi data pada masing-masing kelompok hasil clustering, serta grafik sebaran per cluster yang menggambarkan persebaran data berdasarkan hasil pengelompokan menggunakan metode K-Means. Pada bagian bawah halaman ditampilkan tabel data hasil analisis yang berisi seluruh data beserta label cluster yang diperoleh dari proses clustering. Selain itu, tersedia fitur Pilih Cluster yang memungkinkan Admin untuk memfilter data berdasarkan cluster tertentu sehingga proses analisis dapat dilakukan secara lebih spesifik. Melalui penyajian informasi dalam bentuk ringkasan, visualisasi, dan tabel data, halaman ini membantu Admin dalam memahami karakteristik setiap cluster, mengidentifikasi pola gangguan listrik, serta mendukung proses evaluasi kinerja penanganan gangguan listrik secara lebih efektif.

\subsubsection{Rancangan Halaman Kelola Akun}
Halaman Kelola Akun merupakan halaman yang digunakan oleh Admin untuk mengelola seluruh akun pengguna yang terdaftar pada sistem. Halaman ini hanya dapat diakses oleh pengguna dengan role Admin, sedangkan Pegawai tidak memiliki hak akses terhadap fitur ini. Melalui halaman Kelola Akun, Admin dapat melakukan pengelolaan akun pengguna mulai dari menambahkan akun baru hingga mengubah informasi akun yang telah terdaftar. Dengan adanya fitur ini, proses administrasi pengguna dapat dilakukan secara terpusat sehingga memudahkan pengelolaan hak akses sesuai dengan peran masing-masing pengguna. Selain itu, halaman ini juga mendukung keamanan sistem dengan memastikan bahwa hanya pengguna yang memiliki akun aktif dan hak akses yang sesuai yang dapat menggunakan fitur-fitur yang tersedia pada aplikasi.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_kelola_akun}
\caption{Wireframe Halaman Kelola Akun}
\label{fig:wf_kelola_akun}
\end{figure}

Pada Gambar 3.21, halaman Kelola Akun menampilkan deskripsi singkat mengenai fungsi pengelolaan akun, tombol "Tambah Pengguna Baru", serta tabel Daftar Pengguna. Tombol "Tambah Pengguna Baru" digunakan oleh Admin untuk membuat akun pengguna baru yang nantinya dapat digunakan untuk mengakses sistem. Sementara itu, tabel Daftar Pengguna menampilkan informasi seluruh akun yang telah terdaftar pada sistem, seperti Nomor Induk Pegawai (NIP) sebagai username, nama lengkap, role, serta aksi yang dapat dilakukan terhadap setiap akun. Melalui halaman ini, Admin dapat mengelola akun pengguna secara terstruktur sehingga hanya pengguna yang memiliki akun terdaftar yang dapat mengakses sistem sesuai dengan hak akses yang dimilikinya.

Untuk menambahkan pengguna baru ke dalam sistem, Admin dapat menekan tombol "Tambah Pengguna Baru" yang terdapat pada halaman Kelola Akun. Setelah tombol tersebut dipilih, sistem akan menampilkan sebuah pop-up form yang digunakan untuk memasukkan informasi akun pengguna baru. Form ini dirancang agar proses penambahan akun dapat dilakukan secara cepat dan terstruktur tanpa harus berpindah ke halaman lain.

\begin{figure}[H]
\centering
\includegraphics[width=0.65\textwidth]{wf_kelola_tambah}
\caption{Wireframe Halaman Kelola Akun (Tambah Pengguna)}
\label{fig:wf_kelola_tambah}
\end{figure}

Pada Gambar 3.22, pop-up Tambah Pengguna Baru menampilkan form yang harus diisi oleh Admin untuk membuat akun pengguna baru. Form tersebut terdiri atas beberapa isian, yaitu Username yang menggunakan Nomor Induk Pegawai (NIP), Nama Lengkap, Password, serta Role yang digunakan untuk menentukan hak akses pengguna sebagai Admin atau Pegawai. Setelah seluruh data diisi, Admin dapat menekan tombol "Simpan Akun" untuk menyimpan data pengguna ke dalam sistem sehingga akun dapat digunakan untuk proses login. Apabila Admin membatalkan proses penambahan akun, tombol "Batal" dapat digunakan untuk menutup pop-up tanpa menyimpan data yang telah diinputkan. Dengan adanya form ini, proses pembuatan akun baru dapat dilakukan secara terstruktur sekaligus memastikan bahwa setiap pengguna memiliki identitas dan hak akses yang sesuai sebelum menggunakan aplikasi.

Setelah proses penambahan akun berhasil dilakukan, data pengguna akan tersimpan ke dalam sistem dan secara otomatis ditampilkan pada tabel Daftar Pengguna. Melalui tabel ini, Admin dapat melihat seluruh akun yang telah terdaftar sekaligus melakukan pengelolaan terhadap setiap akun sesuai kebutuhan. Fitur pengelolaan akun dirancang untuk memudahkan Admin dalam melakukan pemeliharaan data pengguna sehingga informasi akun tetap akurat dan keamanan akses sistem dapat terjaga.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_kelola_edit}
\caption{Wireframe Halaman Kelola Akun (Edit dan Reset Password)}
\label{fig:wf_kelola_edit}
\end{figure}

Berdasarkan Gambar 3.23, tabel Daftar Pengguna menampilkan informasi seluruh akun yang telah berhasil didaftarkan ke dalam sistem. Informasi yang ditampilkan meliputi Username (NIP), Nama Lengkap, dan Role pengguna. Pada kolom Aksi, tersedia tiga fitur utama, yaitu Edit Akun, Reset Password, dan Hapus Akun. Fitur Edit Akun digunakan untuk mengubah informasi pengguna, seperti nama lengkap atau role sesuai kebutuhan. Fitur Reset Password memungkinkan Admin untuk mengatur ulang password pengguna apabila pengguna lupa password atau mengalami kendala saat login. Sementara itu, fitur Hapus Akun digunakan untuk menghapus akun pengguna yang sudah tidak diperlukan atau tidak lagi memiliki hak akses terhadap sistem. Dengan adanya fitur-fitur tersebut, Admin dapat mengelola seluruh akun pengguna secara terpusat sehingga keamanan, validitas data pengguna, dan pengaturan hak akses dalam sistem tetap terjaga.

\subsubsection{Rancangan Halaman Profil Pengguna}
Halaman Profil Pengguna merupakan halaman yang digunakan untuk mengelola informasi akun milik pengguna yang sedang login. Halaman ini dapat diakses oleh Admin maupun Pegawai sebagai sarana untuk memperbarui informasi pribadi tanpa memengaruhi data akun pengguna lain. Tampilan dan fitur yang tersedia pada halaman profil bersifat sama untuk kedua role, sehingga baik Admin maupun Pegawai dapat mengubah nama lengkap dan password akun miliknya sendiri melalui halaman ini. Dengan adanya halaman profil, pengguna dapat menjaga keakuratan identitas akun serta meningkatkan keamanan akun melalui perubahan password secara berkala.

\begin{figure}[H]
\centering
\includegraphics[width=0.75\textwidth]{wf_profil_user}
\caption{Wireframe Halaman Profil Pengguna (Admin dan Pegawai)}
\label{fig:wf_profil_user}
\end{figure}

Pada Gambar 3.24, halaman Profil Pengguna terdiri atas dua bagian utama, yaitu Informasi Profil dan Perbarui Password. Pada bagian Informasi Profil, pengguna dapat melihat Username (NIP) yang digunakan sebagai identitas akun serta memperbarui Nama Lengkap sesuai kebutuhan. Username (NIP) hanya ditampilkan sebagai identitas akun dan tidak dapat diubah oleh pengguna. Selanjutnya, pada bagian Perbarui Password, pengguna dapat mengganti password akun dengan memasukkan password lama, password baru, dan konfirmasi password baru. Setelah seluruh data diisi dengan benar, pengguna dapat menyimpan perubahan yang telah dilakukan. Halaman ini dirancang untuk memberikan kemudahan kepada pengguna dalam mengelola informasi akun pribadinya sekaligus meningkatkan keamanan sistem melalui perubahan password secara mandiri. Karena halaman ini digunakan untuk pengelolaan akun pribadi, tampilan maupun fitur yang tersedia bagi Admin dan Pegawai adalah sama. Perbedaannya hanya terletak pada hak akses masing-masing pengguna terhadap fitur-fitur lain di dalam sistem, sedangkan pengelolaan akun pengguna lain tetap menjadi kewenangan Admin melalui menu Kelola Akun.

\subsection{Teknik Pengujian}
Pengujian sistem dilakukan untuk memastikan bahwa aplikasi yang dikembangkan telah berjalan sesuai dengan kebutuhan fungsional serta mampu mengimplementasikan metode K-Means Clustering dengan baik. Pada penelitian ini, pengujian dilakukan terhadap fungsi-fungsi utama aplikasi dan hasil implementasi metode clustering. Pengujian fungsi aplikasi menggunakan metode Black Box Testing, sedangkan pengujian implementasi metode dilakukan dengan membandingkan hasil clustering yang dihasilkan oleh sistem dengan hasil pengolahan data menggunakan Jupyter Notebook sebagai acuan. Melalui pengujian tersebut diharapkan seluruh fitur aplikasi dapat berjalan sesuai dengan kebutuhan pengguna serta menghasilkan keluaran yang konsisten dengan proses clustering yang telah dirancang.

\subsubsection{Black Box Testing}
Pengujian antarmuka dan fungsionalitas aplikasi dilakukan menggunakan metode Black Box Testing. Metode ini berfokus pada pengujian fungsi sistem berdasarkan masukan (input) dan keluaran (output) tanpa memperhatikan struktur internal atau kode program. Pengujian dilakukan untuk memastikan bahwa setiap fitur pada aplikasi, seperti proses login, pengelolaan akun pengguna, unggah dataset, proses clustering, dashboard, analisis tren, hingga perubahan profil pengguna dapat berjalan sesuai dengan kebutuhan fungsional yang telah dirancang. Hasil pengujian nantinya digunakan untuk mengetahui apakah seluruh fungsi sistem telah memberikan keluaran yang sesuai dengan yang diharapkan.

\subsection{Pengujian Implementasi Metode K-Means Clustering}
Pengujian implementasi metode K-Means Clustering dilakukan untuk memastikan bahwa algoritma yang diimplementasikan pada aplikasi menghasilkan keluaran yang konsisten dengan proses pengolahan data yang telah dilakukan pada tahap perancangan menggunakan Jupyter Notebook. Pengujian dilakukan dengan membandingkan hasil clustering yang dihasilkan oleh aplikasi, meliputi pembentukan label cluster, distribusi data pada setiap cluster, serta visualisasi hasil clustering. Selain itu, dilakukan pengecekan terhadap nilai centroid dan hasil analisis yang ditampilkan pada dashboard maupun halaman analisis tren untuk memastikan bahwa seluruh proses perhitungan telah sesuai dengan implementasi metode K-Means Clustering yang digunakan dalam penelitian.
"""

target_path = r"C:\Users\sitif\.gemini\antigravity-ide\brain\22251f2b-5cd8-4f5c-817d-ee0db471f9cf\scratch\bab3_replacement.tex"
os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    f.write(latex_bab3.strip())

print("Saved replacement file. Length:", len(latex_bab3.strip()))
