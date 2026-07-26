# Sequence Diagram — Sistem Klasifikasi Subsidi Listrik

Diagram berikut dibuat dalam format `mxGraphModel` (draw.io) berdasarkan alur kode aktual pada
`web-klasifikasi-subsidi` (Next.js App Router). Seluruh "backend" pada versi ini masih berupa
mock client-side (lihat `lib/data/mock-api.ts`, `lib/data/store.tsx`) — integrasi Flask/Supabase
nyata direncanakan pada milestone M8+/M9 dan belum digambarkan di sini.

Cara pakai: salin blok XML pada tiap bagian ke draw.io (Extras → Edit Diagram) untuk melihat
visualisasinya.

---

## 1. Sequence Diagram: Login

User memasukkan kredensial di `app/(auth)/login/page.tsx`. Jika cocok dengan `ADMIN_USER`/`ADMIN_PASSWORD`
(`lib/data/seed.ts`), `loginDummy()` (`lib/auth.ts`) mengeset cookie `subsidi_session`, lalu
`router.push("/dashboard")`. Permintaan berikutnya diperiksa oleh `proxy.ts` (route guard Next 16)
berdasarkan keberadaan cookie tersebut.

```xml
<mxGraphModel dx="800" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900" math="0" shadow="0">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />

    <!-- Actors -->
    <mxCell id="a1" value="User" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1"><mxGeometry x="40" y="40" width="140" height="40" as="geometry"/></mxCell>
    <mxCell id="a2" value="LoginPage&#10;(app/(auth)/login/page.tsx)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="240" y="40" width="180" height="40" as="geometry"/></mxCell>
    <mxCell id="a3" value="lib/auth.ts&#10;(loginDummy)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="480" y="40" width="160" height="40" as="geometry"/></mxCell>
    <mxCell id="a4" value="Next Router" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="700" y="40" width="140" height="40" as="geometry"/></mxCell>
    <mxCell id="a5" value="proxy.ts&#10;(route guard)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1"><mxGeometry x="900" y="40" width="160" height="40" as="geometry"/></mxCell>
    <mxCell id="a6" value="Dashboard Page" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="1120" y="40" width="160" height="40" as="geometry"/></mxCell>

    <!-- Lifelines -->
    <mxCell id="l1" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="a1" target="a1"><mxGeometry relative="1" as="geometry"><mxPoint x="110" y="80" as="sourcePoint"/><mxPoint x="110" y="760" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="l2" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="a2" target="a2"><mxGeometry relative="1" as="geometry"><mxPoint x="330" y="80" as="sourcePoint"/><mxPoint x="330" y="760" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="l3" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="a3" target="a3"><mxGeometry relative="1" as="geometry"><mxPoint x="560" y="80" as="sourcePoint"/><mxPoint x="560" y="760" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="l4" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="a4" target="a4"><mxGeometry relative="1" as="geometry"><mxPoint x="770" y="80" as="sourcePoint"/><mxPoint x="770" y="760" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="l5" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="a5" target="a5"><mxGeometry relative="1" as="geometry"><mxPoint x="980" y="80" as="sourcePoint"/><mxPoint x="980" y="760" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="l6" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="a6" target="a6"><mxGeometry relative="1" as="geometry"><mxPoint x="1200" y="80" as="sourcePoint"/><mxPoint x="1200" y="760" as="targetPoint"/></mxGeometry></mxCell>

    <!-- Activations -->
    <mxCell id="act1" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="325" y="120" width="10" height="560" as="geometry"/></mxCell>
    <mxCell id="act2" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="555" y="220" width="10" height="60" as="geometry"/></mxCell>
    <mxCell id="act3" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="765" y="320" width="10" height="60" as="geometry"/></mxCell>
    <mxCell id="act4" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="975" y="420" width="10" height="80" as="geometry"/></mxCell>
    <mxCell id="act5" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1195" y="540" width="10" height="60" as="geometry"/></mxCell>

    <!-- Messages -->
    <mxCell id="m1" value="1: isi email + password, submit" style="html=1;endArrow=block;elbow=vertical;startArrow=none;fontSize=11;" edge="1" parent="1" source="a1" target="act1"><mxGeometry relative="1" as="geometry"><mxPoint x="110" y="120" as="sourcePoint"/></mxGeometry></mxCell>
    <mxCell id="m2" value="2: validasi form (email &amp; password terisi)" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="330" y="150" as="sourcePoint"/><mxPoint x="330" y="150" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="m3" value="3: bandingkan dgn ADMIN_USER / ADMIN_PASSWORD (seed.ts)" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="330" y="190" as="sourcePoint"/><mxPoint x="330" y="190" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="m4" value="4: loginDummy() — set cookie subsidi_session" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="act1" target="act2"><mxGeometry relative="1" as="geometry"><mxPoint x="330" y="220" as="sourcePoint"/><mxPoint x="560" y="220" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="m5" value="5: cookie tersimpan (return)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="act2" target="act1"><mxGeometry relative="1" as="geometry"><mxPoint x="560" y="270" as="sourcePoint"/><mxPoint x="330" y="270" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="m6" value="6: router.push('/dashboard') + router.refresh()" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="act1" target="act3"><mxGeometry relative="1" as="geometry"><mxPoint x="330" y="320" as="sourcePoint"/><mxPoint x="770" y="320" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="m7" value="7: navigasi ke /dashboard" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="act3" target="act4"><mxGeometry relative="1" as="geometry"><mxPoint x="770" y="380" as="sourcePoint"/><mxPoint x="980" y="380" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="m8" value="8: cek cookie subsidi_session pada request" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="980" y="440" as="sourcePoint"/><mxPoint x="980" y="440" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="m9" value="9: cookie valid → izinkan (lanjutkan ke route)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="act4" target="act5"><mxGeometry relative="1" as="geometry"><mxPoint x="980" y="500" as="sourcePoint"/><mxPoint x="1200" y="500" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="m10" value="10: render Dashboard" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="act5" target="a1"><mxGeometry relative="1" as="geometry"><mxPoint x="1200" y="560" as="sourcePoint"/><mxPoint x="110" y="560" as="targetPoint"/></mxGeometry></mxCell>

    <mxCell id="alt1" value="alt: kredensial salah" style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=none;strokeColor=#b85450;fontSize=11;dashed=1;" vertex="1" parent="1"><mxGeometry x="270" y="620" width="180" height="80" as="geometry"/></mxCell>
    <mxCell id="m11" value="setError('Email atau password salah. Coba lagi.')" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="330" y="660" as="sourcePoint"/><mxPoint x="330" y="660" as="targetPoint"/></mxGeometry></mxCell>
  </root>
</mxGraphModel>
```

---

## 2. Sequence Diagram: Klasifikasi Manual

User mengisi form 9 variabel pada `KlasifikasiBaruPage` (`app/(dashboard)/klasifikasi/baru/page.tsx`)
lalu menekan "Jalankan Klasifikasi" → `runManual()` → `predictRow(row)` (`lib/data/mock-api.ts`, memanggil
`scoreRow(row)` untuk menghitung skor heuristik) → `commitPrediction()` men-dispatch `addPrediction`
ke `Store` (`lib/data/store.tsx`, persist ke `localStorage`) dan mencatat `addActivity()` → router
push ke halaman hasil (`klasifikasi/hasil/[predictionId]/page.tsx`) yang membaca data dari Store.

```xml
<mxGraphModel dx="800" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="1000" math="0" shadow="0">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />

    <!-- Actors -->
    <mxCell id="b1" value="User" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1"><mxGeometry x="20" y="40" width="130" height="40" as="geometry"/></mxCell>
    <mxCell id="b2" value="KlasifikasiBaruPage&#10;(runManual)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="200" y="40" width="180" height="40" as="geometry"/></mxCell>
    <mxCell id="b3" value="mock-api.ts&#10;(predictRow)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="430" y="40" width="160" height="40" as="geometry"/></mxCell>
    <mxCell id="b4" value="mock-api.ts&#10;(scoreRow)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="640" y="40" width="160" height="40" as="geometry"/></mxCell>
    <mxCell id="b5" value="commitPrediction()&#10;(dlm page.tsx)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="850" y="40" width="170" height="40" as="geometry"/></mxCell>
    <mxCell id="b6" value="Store&#10;(store.tsx, dispatch)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1"><mxGeometry x="1070" y="40" width="160" height="40" as="geometry"/></mxCell>
    <mxCell id="b7" value="localStorage&#10;(klasifikasi-subsidi-store-v1)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1"><mxGeometry x="1280" y="40" width="190" height="40" as="geometry"/></mxCell>
    <mxCell id="b8" value="HasilPredictionPage&#10;(hasil/[predictionId])" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="1520" y="40" width="180" height="40" as="geometry"/></mxCell>

    <!-- Lifelines -->
    <mxCell id="bl1" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="b1" target="b1"><mxGeometry relative="1" as="geometry"><mxPoint x="85" y="80" as="sourcePoint"/><mxPoint x="85" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bl2" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="b2" target="b2"><mxGeometry relative="1" as="geometry"><mxPoint x="290" y="80" as="sourcePoint"/><mxPoint x="290" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bl3" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="b3" target="b3"><mxGeometry relative="1" as="geometry"><mxPoint x="510" y="80" as="sourcePoint"/><mxPoint x="510" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bl4" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="b4" target="b4"><mxGeometry relative="1" as="geometry"><mxPoint x="720" y="80" as="sourcePoint"/><mxPoint x="720" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bl5" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="b5" target="b5"><mxGeometry relative="1" as="geometry"><mxPoint x="935" y="80" as="sourcePoint"/><mxPoint x="935" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bl6" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="b6" target="b6"><mxGeometry relative="1" as="geometry"><mxPoint x="1150" y="80" as="sourcePoint"/><mxPoint x="1150" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bl7" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="b7" target="b7"><mxGeometry relative="1" as="geometry"><mxPoint x="1375" y="80" as="sourcePoint"/><mxPoint x="1375" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bl8" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="b8" target="b8"><mxGeometry relative="1" as="geometry"><mxPoint x="1610" y="80" as="sourcePoint"/><mxPoint x="1610" y="920" as="targetPoint"/></mxGeometry></mxCell>

    <!-- Activations -->
    <mxCell id="bact2" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="285" y="120" width="10" height="740" as="geometry"/></mxCell>
    <mxCell id="bact3" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="505" y="220" width="10" height="140" as="geometry"/></mxCell>
    <mxCell id="bact4" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="715" y="260" width="10" height="60" as="geometry"/></mxCell>
    <mxCell id="bact5" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="930" y="400" width="10" height="260" as="geometry"/></mxCell>
    <mxCell id="bact6" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1145" y="440" width="10" height="100" as="geometry"/></mxCell>
    <mxCell id="bact7" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1370" y="480" width="10" height="40" as="geometry"/></mxCell>
    <mxCell id="bact8" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1605" y="700" width="10" height="140" as="geometry"/></mxCell>

    <!-- Messages -->
    <mxCell id="bm1" value="1: isi 9 variabel form, klik 'Jalankan Klasifikasi'" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="b1" target="bact2"><mxGeometry relative="1" as="geometry"><mxPoint x="85" y="120" as="sourcePoint"/><mxPoint x="290" y="120" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm2" value="2: validate(form) — cek 9 field wajib" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="290" y="160" as="sourcePoint"/><mxPoint x="290" y="160" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm3" value="3: bangun CustomerRow (id_pelanggan: MAN-xxxxxx)" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="290" y="190" as="sourcePoint"/><mxPoint x="290" y="190" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm4" value="4: predictRow(row)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="bact2" target="bact3"><mxGeometry relative="1" as="geometry"><mxPoint x="290" y="220" as="sourcePoint"/><mxPoint x="510" y="220" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm5" value="5: scoreRow(row)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="bact3" target="bact4"><mxGeometry relative="1" as="geometry"><mxPoint x="510" y="260" as="sourcePoint"/><mxPoint x="720" y="260" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm6" value="6: skor 0..1 (jumlah bobot 5 faktor)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="bact4" target="bact3"><mxGeometry relative="1" as="geometry"><mxPoint x="720" y="310" as="sourcePoint"/><mxPoint x="510" y="310" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm7" value="7: label (Layak/Tidak Layak) + confidence" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="bact3" target="bact2"><mxGeometry relative="1" as="geometry"><mxPoint x="510" y="350" as="sourcePoint"/><mxPoint x="290" y="350" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm8" value="8: commitPrediction([hasil], 'manual')" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="bact2" target="bact5"><mxGeometry relative="1" as="geometry"><mxPoint x="290" y="400" as="sourcePoint"/><mxPoint x="935" y="400" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm9" value="9: dispatch({type:'addPrediction', prediction})" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="bact5" target="bact6"><mxGeometry relative="1" as="geometry"><mxPoint x="935" y="440" as="sourcePoint"/><mxPoint x="1150" y="440" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm10" value="10: reducer update state.predictions" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="1150" y="470" as="sourcePoint"/><mxPoint x="1150" y="470" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm11" value="11: persist state → setItem(store-v1)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="bact6" target="bact7"><mxGeometry relative="1" as="geometry"><mxPoint x="1150" y="480" as="sourcePoint"/><mxPoint x="1375" y="480" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm12" value="12: addActivity('prediksi', 'Klasifikasi manual 1 pelanggan dijalankan')" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="bact5" target="bact6"><mxGeometry relative="1" as="geometry"><mxPoint x="935" y="540" as="sourcePoint"/><mxPoint x="1150" y="540" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm13" value="13: router.push('/klasifikasi/hasil/{id}')" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="bact5" target="bact8"><mxGeometry relative="1" as="geometry"><mxPoint x="935" y="620" as="sourcePoint"/><mxPoint x="1610" y="620" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm14" value="14: baca prediction by id dari Store" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="bact8" target="bact6"><mxGeometry relative="1" as="geometry"><mxPoint x="1610" y="700" as="sourcePoint"/><mxPoint x="1150" y="700" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="bm15" value="15: render hasil klasifikasi (label, confidence)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="bact8" target="b1"><mxGeometry relative="1" as="geometry"><mxPoint x="1610" y="800" as="sourcePoint"/><mxPoint x="85" y="800" as="targetPoint"/></mxGeometry></mxCell>
  </root>
</mxGraphModel>
```

---

## 3. Sequence Diagram: Klasifikasi Batch (CSV)

Dari tab "Upload Batch" pada `KlasifikasiBaruPage`, user memilih file CSV via `FileDropzone` lalu
menekan "Jalankan Klasifikasi" → `runBatch()` → `parseCustomerCsv(file)` (`lib/data/csv.ts`)
mengubah isi CSV menjadi `CustomerRow[]` → `predictRows(rows)` (`lib/data/mock-api.ts`, memanggil
`predictRow`/`scoreRow` per baris) → `commitPrediction()` men-dispatch hasil batch ke `Store`
(persist localStorage) → router push ke halaman hasil.

```xml
<mxGraphModel dx="800" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1900" pageHeight="1000" math="0" shadow="0">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />

    <!-- Actors -->
    <mxCell id="c1" value="User" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1"><mxGeometry x="20" y="40" width="120" height="40" as="geometry"/></mxCell>
    <mxCell id="c2" value="KlasifikasiBaruPage&#10;(runBatch)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="190" y="40" width="170" height="40" as="geometry"/></mxCell>
    <mxCell id="c3" value="FileDropzone" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="400" y="40" width="150" height="40" as="geometry"/></mxCell>
    <mxCell id="c4" value="lib/data/csv.ts&#10;(parseCustomerCsv)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="590" y="40" width="180" height="40" as="geometry"/></mxCell>
    <mxCell id="c5" value="mock-api.ts&#10;(predictRows)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="810" y="40" width="170" height="40" as="geometry"/></mxCell>
    <mxCell id="c6" value="mock-api.ts&#10;(predictRow / scoreRow)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="1020" y="40" width="190" height="40" as="geometry"/></mxCell>
    <mxCell id="c7" value="commitPrediction()" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="1250" y="40" width="160" height="40" as="geometry"/></mxCell>
    <mxCell id="c8" value="Store + localStorage" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1"><mxGeometry x="1450" y="40" width="170" height="40" as="geometry"/></mxCell>
    <mxCell id="c9" value="HasilPredictionPage" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="1670" y="40" width="170" height="40" as="geometry"/></mxCell>

    <!-- Lifelines -->
    <mxCell id="cl1" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c1" target="c1"><mxGeometry relative="1" as="geometry"><mxPoint x="80" y="80" as="sourcePoint"/><mxPoint x="80" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cl2" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c2" target="c2"><mxGeometry relative="1" as="geometry"><mxPoint x="275" y="80" as="sourcePoint"/><mxPoint x="275" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cl3" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c3" target="c3"><mxGeometry relative="1" as="geometry"><mxPoint x="475" y="80" as="sourcePoint"/><mxPoint x="475" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cl4" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c4" target="c4"><mxGeometry relative="1" as="geometry"><mxPoint x="680" y="80" as="sourcePoint"/><mxPoint x="680" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cl5" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c5" target="c5"><mxGeometry relative="1" as="geometry"><mxPoint x="895" y="80" as="sourcePoint"/><mxPoint x="895" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cl6" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c6" target="c6"><mxGeometry relative="1" as="geometry"><mxPoint x="1115" y="80" as="sourcePoint"/><mxPoint x="1115" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cl7" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c7" target="c7"><mxGeometry relative="1" as="geometry"><mxPoint x="1330" y="80" as="sourcePoint"/><mxPoint x="1330" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cl8" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c8" target="c8"><mxGeometry relative="1" as="geometry"><mxPoint x="1535" y="80" as="sourcePoint"/><mxPoint x="1535" y="920" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cl9" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="c9" target="c9"><mxGeometry relative="1" as="geometry"><mxPoint x="1755" y="80" as="sourcePoint"/><mxPoint x="1755" y="920" as="targetPoint"/></mxGeometry></mxCell>

    <!-- Activations -->
    <mxCell id="cact2" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="270" y="120" width="10" height="740" as="geometry"/></mxCell>
    <mxCell id="cact3" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="470" y="120" width="10" height="60" as="geometry"/></mxCell>
    <mxCell id="cact4" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="675" y="240" width="10" height="80" as="geometry"/></mxCell>
    <mxCell id="cact5" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="890" y="360" width="10" height="140" as="geometry"/></mxCell>
    <mxCell id="cact6" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1110" y="400" width="10" height="60" as="geometry"/></mxCell>
    <mxCell id="cact7" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1325" y="540" width="10" height="240" as="geometry"/></mxCell>
    <mxCell id="cact8" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1530" y="580" width="10" height="140" as="geometry"/></mxCell>
    <mxCell id="cact9" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1750" y="780" width="10" height="120" as="geometry"/></mxCell>

    <!-- Messages -->
    <mxCell id="cm1" value="1: pilih file .csv" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="c1" target="cact3"><mxGeometry relative="1" as="geometry"><mxPoint x="80" y="120" as="sourcePoint"/><mxPoint x="475" y="120" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm2" value="2: onFile(file) → set state file" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="cact3" target="cact2"><mxGeometry relative="1" as="geometry"><mxPoint x="475" y="160" as="sourcePoint"/><mxPoint x="275" y="160" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm3" value="3: klik 'Jalankan Klasifikasi' → runBatch()" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="c1" target="cact2"><mxGeometry relative="1" as="geometry"><mxPoint x="80" y="200" as="sourcePoint"/><mxPoint x="275" y="200" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm4" value="4: parseCustomerCsv(file)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="cact2" target="cact4"><mxGeometry relative="1" as="geometry"><mxPoint x="275" y="240" as="sourcePoint"/><mxPoint x="680" y="240" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm5" value="5: parse header + baris CSV → CustomerRow[]" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="680" y="270" as="sourcePoint"/><mxPoint x="680" y="270" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm6" value="6: rows: CustomerRow[] (return)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="cact4" target="cact2"><mxGeometry relative="1" as="geometry"><mxPoint x="680" y="320" as="sourcePoint"/><mxPoint x="275" y="320" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm7" value="7: predictRows(rows)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="cact2" target="cact5"><mxGeometry relative="1" as="geometry"><mxPoint x="275" y="360" as="sourcePoint"/><mxPoint x="895" y="360" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm8" value="8: loop: predictRow(row) → scoreRow(row)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="cact5" target="cact6"><mxGeometry relative="1" as="geometry"><mxPoint x="895" y="400" as="sourcePoint"/><mxPoint x="1115" y="400" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm9" value="9: label + confidence per baris (return)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="cact6" target="cact5"><mxGeometry relative="1" as="geometry"><mxPoint x="1115" y="440" as="sourcePoint"/><mxPoint x="895" y="440" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm10" value="10: PredictionResultRow[] (hasil batch)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="cact5" target="cact2"><mxGeometry relative="1" as="geometry"><mxPoint x="895" y="480" as="sourcePoint"/><mxPoint x="275" y="480" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm11" value="11: commitPrediction(hasil, 'batch', file.name)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="cact2" target="cact7"><mxGeometry relative="1" as="geometry"><mxPoint x="275" y="540" as="sourcePoint"/><mxPoint x="1330" y="540" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm12" value="12: dispatch({type:'addPrediction'}) + addActivity('batch ...')" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="cact7" target="cact8"><mxGeometry relative="1" as="geometry"><mxPoint x="1330" y="580" as="sourcePoint"/><mxPoint x="1535" y="580" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm13" value="13: persist ke localStorage (store-v1)" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="1535" y="620" as="sourcePoint"/><mxPoint x="1535" y="620" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm14" value="14: router.push('/klasifikasi/hasil/{id}')" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="cact7" target="cact9"><mxGeometry relative="1" as="geometry"><mxPoint x="1330" y="700" as="sourcePoint"/><mxPoint x="1755" y="700" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm15" value="15: baca prediction batch dari Store" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="cact9" target="cact8"><mxGeometry relative="1" as="geometry"><mxPoint x="1755" y="780" sourcePoint="1"/><mxPoint x="1535" y="780" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="cm16" value="16: render ringkasan (jumlah Layak / Tidak Layak) + tabel hasil" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="cact9" target="c1"><mxGeometry relative="1" as="geometry"><mxPoint x="1755" y="880" as="sourcePoint"/><mxPoint x="80" y="880" as="targetPoint"/></mxGeometry></mxCell>
  </root>
</mxGraphModel>
```

---

## 4. Sequence Diagram: Lihat Laporan

User membuka `app/(dashboard)/laporan/page.tsx` (`LaporanPage`) yang membaca `state.reports` dari
`useStore()` dan menampilkan daftar laporan (dengan filter tanggal `dateFrom`/`dateTo`). Saat user
mengklik salah satu baris, navigasi menuju `app/(dashboard)/laporan/[id]/page.tsx` yang membaca
detail laporan dari Store berdasarkan `id` (via `useParams()`) dan menampilkannya.

```xml
<mxGraphModel dx="800" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="800" math="0" shadow="0">
  <root>
    <mxCell id="0" />
    <mxCell id="1" parent="0" />

    <!-- Actors -->
    <mxCell id="d1" value="User" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1"><mxGeometry x="20" y="40" width="120" height="40" as="geometry"/></mxCell>
    <mxCell id="d2" value="LaporanPage&#10;(laporan/page.tsx)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="220" y="40" width="180" height="40" as="geometry"/></mxCell>
    <mxCell id="d3" value="Store&#10;(useStore, store.tsx)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1"><mxGeometry x="470" y="40" width="180" height="40" as="geometry"/></mxCell>
    <mxCell id="d4" value="Next Router / Link" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1"><mxGeometry x="720" y="40" width="160" height="40" as="geometry"/></mxCell>
    <mxCell id="d5" value="LaporanDetailPage&#10;(laporan/[id]/page.tsx)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1"><mxGeometry x="950" y="40" width="200" height="40" as="geometry"/></mxCell>

    <!-- Lifelines -->
    <mxCell id="dl1" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="d1" target="d1"><mxGeometry relative="1" as="geometry"><mxPoint x="80" y="80" as="sourcePoint"/><mxPoint x="80" y="740" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dl2" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="d2" target="d2"><mxGeometry relative="1" as="geometry"><mxPoint x="310" y="80" as="sourcePoint"/><mxPoint x="310" y="740" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dl3" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="d3" target="d3"><mxGeometry relative="1" as="geometry"><mxPoint x="560" y="80" as="sourcePoint"/><mxPoint x="560" y="740" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dl4" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="d4" target="d4"><mxGeometry relative="1" as="geometry"><mxPoint x="800" y="80" as="sourcePoint"/><mxPoint x="800" y="740" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dl5" style="endArrow=none;dashed=1;html=1;strokeColor=#999999;" edge="1" parent="1" source="d5" target="d5"><mxGeometry relative="1" as="geometry"><mxPoint x="1050" y="80" as="sourcePoint"/><mxPoint x="1050" y="740" as="targetPoint"/></mxGeometry></mxCell>

    <!-- Activations -->
    <mxCell id="dact2" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="305" y="120" width="10" height="200" as="geometry"/></mxCell>
    <mxCell id="dact3a" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="555" y="160" width="10" height="60" as="geometry"/></mxCell>
    <mxCell id="dact5" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="1045" y="480" width="10" height="200" as="geometry"/></mxCell>
    <mxCell id="dact3b" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;" vertex="1" parent="1"><mxGeometry x="555" y="540" width="10" height="60" as="geometry"/></mxCell>

    <!-- Messages -->
    <mxCell id="dm1" value="1: buka halaman /laporan" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="d1" target="dact2"><mxGeometry relative="1" as="geometry"><mxPoint x="80" y="120" as="sourcePoint"/><mxPoint x="310" y="120" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm2" value="2: useStore() → baca state.reports" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="dact2" target="dact3a"><mxGeometry relative="1" as="geometry"><mxPoint x="310" y="160" as="sourcePoint"/><mxPoint x="560" y="160" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm3" value="3: reports[] (return, hydrated=true)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="dact3a" target="dact2"><mxGeometry relative="1" as="geometry"><mxPoint x="560" y="210" as="sourcePoint"/><mxPoint x="310" y="210" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm4" value="4: filter by dateFrom/dateTo (client-side)" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="310" y="250" as="sourcePoint"/><mxPoint x="310" y="250" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm5" value="5: render tabel daftar laporan" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="dact2" target="d1"><mxGeometry relative="1" as="geometry"><mxPoint x="310" y="300" as="sourcePoint"/><mxPoint x="80" y="300" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm6" value="6: klik salah satu baris laporan (Link)" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="d1" target="d4"><mxGeometry relative="1" as="geometry"><mxPoint x="80" y="400" as="sourcePoint"/><mxPoint x="800" y="400" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm7" value="7: navigasi ke /laporan/{id}" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="d4" target="dact5"><mxGeometry relative="1" as="geometry"><mxPoint x="800" y="440" as="sourcePoint"/><mxPoint x="1050" y="440" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm8" value="8: useParams() → id" style="html=1;endArrow=none;dashed=1;fontSize=10;fontColor=#666666;" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="1050" y="500" as="sourcePoint"/><mxPoint x="1050" y="500" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm9" value="9: useStore() → cari report by id" style="html=1;endArrow=block;fontSize=11;" edge="1" parent="1" source="dact5" target="dact3b"><mxGeometry relative="1" as="geometry"><mxPoint x="1050" y="540" as="sourcePoint"/><mxPoint x="560" y="540" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm10" value="10: report detail (return)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="dact3b" target="dact5"><mxGeometry relative="1" as="geometry"><mxPoint x="560" y="590" as="sourcePoint"/><mxPoint x="1050" y="590" as="targetPoint"/></mxGeometry></mxCell>
    <mxCell id="dm11" value="11: render detail laporan (ringkasan, tabel hasil)" style="html=1;endArrow=open;dashed=1;fontSize=11;" edge="1" parent="1" source="dact5" target="d1"><mxGeometry relative="1" as="geometry"><mxPoint x="1050" y="660" as="sourcePoint"/><mxPoint x="80" y="660" as="targetPoint"/></mxGeometry></mxCell>
  </root>
</mxGraphModel>
```
