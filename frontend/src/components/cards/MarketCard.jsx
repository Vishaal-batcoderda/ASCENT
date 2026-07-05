import GlassCard from "../ui/GlassCard";

function MarketCard({ market }) {

    return (

        <GlassCard>

            <h2 className="text-xl font-semibold mb-5">
                Market Overview
            </h2>

            {
                market ? (

                    <div className="space-y-3">

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                Company
                            </span>

                            <span>
                                {market.company}
                            </span>
                        </div>

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                Price
                            </span>

                            <span>
                                ${market.current_price}
                            </span>
                        </div>

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                Volume
                            </span>

                            <span>
                                {market.volume.toLocaleString()}
                            </span>
                        </div>

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                52W High
                            </span>

                            <span>
                                ${market.high_52_week}
                            </span>
                        </div>

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                52W Low
                            </span>

                            <span>
                                ${market.low_52_week}
                            </span>
                        </div>

                    </div>

                ) : (

                    <p className="text-slate-500">
                        Analyze a stock to view market data.
                    </p>

                )
            }

        </GlassCard>

    );

}

export default MarketCard;