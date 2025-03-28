import Analyzer from "@/components/Analyzer";
import GetMoney from "@/components/Getter";

export default function Home() {
  return (
    <div>
      <Analyzer url="https://raw.githubusercontent.com/ahmetcanisik/learn/refs/heads/main/README.md" />
      <GetMoney url="https://www.trendyol.com/pd/realme/8-kilif-hd-baskili-kilif-followed-organization-5158-p-903290548?boutiqueId=61&merchantId=817318" />
    </div>
  );
}
