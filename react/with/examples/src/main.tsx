import { createRoot } from 'react-dom/client'
import '@/styles/global.css'
import App from './App.tsx'
import {BrowserRouter, Routes, Route} from "react-router";
import {Calculator, Captcha} from "@/apps";

createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <Routes>
        <Route path="/" element={<App />} />
        <Route path="/calculator" element={<Calculator />} />
        <Route path="/captcha" element={<Captcha />} />
    </Routes>
  </BrowserRouter>,
)
