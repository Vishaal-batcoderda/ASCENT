import GlassCard from "../ui/GlassCard";

function TechnicalCard({ technical }) {

    return (

        <GlassCard>

            <h2 className="text-xl font-semibold mb-5">
                Technical Indicators
            </h2>

            {
                technical ? (

                    <div className="space-y-3">

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                SMA (20)
                            </span>

                            <span>
                                {technical.sma}
                            </span>
                        </div>

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                EMA (20)
                            </span>

                            <span>
                                {technical.ema}
                            </span>
                        </div>

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                RSI (14)
                            </span>

                            <span>
                                {technical.rsi}
                            </span>
                        </div>

                        <div className="flex justify-between">
                            <span className="text-slate-400">
                                MACD
                            </span>

                            <span>
                                {technical.macd}
                            </span>
                        </div>

                    </div>

                ) : (

                    <p className="text-slate-500">
                        Analyze a stock to view technical indicators.
                    </p>

                )
            }

        </GlassCard>

    );

}

export default TechnicalCard;